"""
================================================================================
  🌐 ADVANCED ENGLISH TO HINDI TRANSLATOR & LINGUISTIC RESEARCH STUDIO 📚
================================================================================
  ALL-IN-ONE STANDALONE PYTHON APPLICATION (ZERO EXTERNAL PIP PACKAGES REQUIRED)

  KEY CAPABILITIES:
  -----------------
  1. 🌐 Real-Time Bidirectional Translation (English ➔ Hindi & Hindi ➔ English)
  2. 🔍 Deep Word Research & Linguistic Analysis (via Free Dictionary & Datamuse APIs)
      - International Phonetic Alphabet (IPA) Phonetics
      - Native Windows Text-To-Speech (TTS) Voice Audio Pronunciation
      - Grammatical Parts of Speech Breakdown (Noun, Verb, Adjective, Adverb, etc.)
      - Granular English Definitions & Contextual Real-World Example Sentences
      - Contextual Hindi Translation & Hinglish Phonetic Transliteration
      - Semantic Relations (Synonyms, Antonyms, Rhymes, Descriptive Collocations)
      - Alternative Contextual Meanings & Confidence Match Scores
  3. 📦 Embedded Lexicon Database (Works fully offline with rich built-in vocabulary)
  4. 🧠 Interactive Hindi-English Vocabulary Quiz Challenge Game
  5. 📊 Batch Word Research & Study Flashcard Builder
  6. 📜 Search History, Starred Bookmarks & Exporters (Markdown Study Notes & CSV)
  7. 🖥️  Modern Desktop Graphical User Interface (Tkinter Studio with Dark Theme)
================================================================================
"""

import sys
import os
import json
import time
import subprocess
import urllib.request
import urllib.parse
import urllib.error
import concurrent.futures
import threading
import argparse
import csv
import webbrowser
from typing import Dict, List, Any, Optional

# Configure standard I/O for UTF-8 encoding (supporting Devanagari Hindi on Windows)
if sys.stdout and hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

if sys.stderr and hasattr(sys.stderr, "reconfigure"):
    try:
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

# Enable ANSI colors on Windows console
if os.name == 'nt':
    os.system('')


# ==============================================================================
# 1. TERMINAL STYLING & FORMATTING
# ==============================================================================

class Colors:
    """ANSI terminal styling escape codes."""
    RESET = "\033[0m"
    BOLD = "\033[1m"
    DIM = "\033[2m"
    ITALIC = "\033[3m"
    UNDERLINE = "\033[4m"
    
    BLACK = "\033[30m"
    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    BLUE = "\033[94m"
    MAGENTA = "\033[95m"
    CYAN = "\033[96m"
    WHITE = "\033[97m"
    
    BG_BLUE = "\033[44m"
    BG_DARK = "\033[100m"


def print_banner():
    """Prints the application visual banner."""
    banner = f"""{Colors.CYAN}{Colors.BOLD}
╔══════════════════════════════════════════════════════════════════════════════╗
║      🌐 ENGLISH ➔ HINDI TRANSLATOR & LINGUISTIC RESEARCH STUDIO 📚          ║
║      Deep Word Analysis • Definitions • Phonetics • Synonyms • Quiz & GUI    ║
╚══════════════════════════════════════════════════════════════════════════════╝{Colors.RESET}"""
    print(banner)


# ==============================================================================
# 2. NATIVE AUDIO PRONUNCIATION / SPEECH SYNTHESIS ENGINE
# ==============================================================================

class AudioSpeechEngine:
    """Provides native text-to-speech voice pronunciation without external pip packages."""
    
    @staticmethod
    def speak(text: str, is_async: bool = True):
        """Speaks English text using native Windows SAPI speech synthesizer."""
        if not text:
            return
            
        def _runner():
            clean_text = text.replace("'", "").replace('"', '').replace('\n', ' ')
            if os.name == 'nt':
                try:
                    ps_cmd = f"Add-Type -AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('{clean_text}')"
                    subprocess.run(["powershell", "-Command", ps_cmd], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=8)
                except Exception:
                    pass
                    
        if is_async:
            threading.Thread(target=_runner, daemon=True).start()
        else:
            _runner()


# ==============================================================================
# 3. HINGLISH TRANSLITERATION ENGINE
# ==============================================================================

class HinglishTransliterator:
    """Converts Devanagari Hindi text to Romanized / Hinglish phonetic spelling."""
    
    VOWELS = {
        'अ': 'a', 'आ': 'aa', 'इ': 'i', 'ई': 'ee', 'उ': 'u', 'ऊ': 'oo', 'ऋ': 'ri',
        'ए': 'e', 'ऐ': 'ai', 'ओ': 'o', 'औ': 'au', 'अं': 'an', 'अः': 'ah'
    }
    
    MATRAS = {
        'ा': 'aa', 'ि': 'i', 'ी': 'ee', 'ु': 'u', 'ू': 'oo', 'ृ': 'ri',
        'े': 'e', 'ै': 'ai', 'ो': 'o', 'ौ': 'au', 'ं': 'n', 'ँ': 'n', 'ः': 'h', '्': ''
    }
    
    CONSONANTS = {
        'क': 'k', 'ख': 'kh', 'ग': 'g', 'घ': 'gh', 'ङ': 'ng',
        'च': 'ch', 'छ': 'chh', 'ज': 'j', 'झ': 'jh', 'ञ': 'ny',
        'ट': 't', 'ठ': 'th', 'ड': 'd', 'ढ': 'dh', 'ण': 'n',
        'त': 't', 'थ': 'th', 'द': 'd', 'ध': 'dh', 'न': 'n',
        'प': 'p', 'फ': 'ph', 'ब': 'b', 'भ': 'bh', 'म': 'm',
        'य': 'y', 'र': 'r', 'ल': 'l', 'व': 'v', 'श': 'sh', 'ष': 'sh', 'स': 's', 'ह': 'h',
        'क्ष': 'ksh', 'त्र': 'tra', 'ज्ञ': 'gya', 'ड़': 'd', 'ढ़': 'dh', 'ज़': 'z', 'फ़': 'f'
    }
    
    @classmethod
    def transliterate(cls, text: str) -> str:
        """Transliterates Devanagari text to readable phonetic Latin script."""
        if not text:
            return ""
        result = []
        i = 0
        n = len(text)
        while i < n:
            char = text[i]
            if char in cls.VOWELS:
                result.append(cls.VOWELS[char])
            elif char in cls.CONSONANTS:
                if i + 1 < n and text[i+1] in cls.MATRAS:
                    result.append(cls.CONSONANTS[char] + cls.MATRAS[text[i+1]])
                    i += 1
                elif i + 1 < n and text[i+1] == '़': # Nukta
                    nukta_char = char + '़'
                    mapped = cls.CONSONANTS.get(nukta_char, cls.CONSONANTS[char])
                    if i + 2 < n and text[i+2] in cls.MATRAS:
                        result.append(mapped + cls.MATRAS[text[i+2]])
                        i += 2
                    else:
                        result.append(mapped + ('a' if i + 2 < n and text[i+2] in cls.CONSONANTS else ''))
                        i += 1
                else:
                    if i + 1 < n and (text[i+1] in cls.CONSONANTS or text[i+1] in cls.VOWELS):
                        result.append(cls.CONSONANTS[char] + 'a')
                    else:
                        result.append(cls.CONSONANTS[char])
            elif char in cls.MATRAS:
                result.append(cls.MATRAS[char])
            else:
                result.append(char)
            i += 1
        return ''.join(result).strip().capitalize()


# ==============================================================================
# 4. BUILT-IN OFFLINE LEXICON & VOCABULARY DOSSIERS
# ==============================================================================

EMBEDDED_VOCABULARY_DATABASE = {
    "perseverance": {
        "hindi": "दृढ़ता / लगन",
        "hinglish": "Dridhta / Lagan",
        "ipa": "ˌpɜːsɪˈvɪərəns",
        "pos": "noun",
        "definition": "Persistence in doing something despite difficulty or delay in achieving success.",
        "example": "His perseverance helped him overcome all hurdles and succeed.",
        "synonyms": ["persistence", "tenacity", "determination", "grit", "steadfastness"],
        "antonyms": ["hesitation", "apathy", "giving up", "irresolution"],
        "rhymes": ["coherence", "appearance", "adherence", "clearance"]
    },
    "eloquent": {
        "hindi": "सुवक्ता / भावपूर्ण",
        "hinglish": "Suvakta / Bhaavpoorna",
        "ipa": "ˈɛləkwənt",
        "pos": "adjective",
        "definition": "Fluent or persuasive in speaking or writing.",
        "example": "She gave an eloquent speech that moved the entire audience.",
        "synonyms": ["articulate", "fluent", "persuasive", "expressive", "silver-tongued"],
        "antonyms": ["inarticulate", "hesitant", "mute", "tongue-tied"],
        "rhymes": ["reluctant"]
    },
    "courage": {
        "hindi": "साहस / हिम्मत",
        "hinglish": "Saahas / Himmat",
        "ipa": "ˈkʌrɪdʒ",
        "pos": "noun",
        "definition": "The ability to do something that frightens one; bravery.",
        "example": "She showed immense courage in the face of adversity.",
        "synonyms": ["bravery", "valor", "fearlessness", "audacity", "heroism"],
        "antonyms": ["cowardice", "fear", "timidity", "faint-heartedness"],
        "rhymes": ["discourage", "encourage"]
    },
    "knowledge": {
        "hindi": "ज्ञान / विद्या",
        "hinglish": "Gyaan / Vidya",
        "ipa": "ˈnɒlɪdʒ",
        "pos": "noun",
        "definition": "Facts, information, and skills acquired through experience or education.",
        "example": "Knowledge is the greatest power a human can possess.",
        "synonyms": ["wisdom", "understanding", "intelligence", "insight", "erudition"],
        "antonyms": ["ignorance", "illiteracy", "inexperience"],
        "rhymes": ["acknowledge"]
    },
    "gratitude": {
        "hindi": "कृतज्ञता / आभार",
        "hinglish": "Kritagyata / Aabhaar",
        "ipa": "ˈɡrætɪtjuːd",
        "pos": "noun",
        "definition": "The quality of being thankful; readiness to show appreciation.",
        "example": "He expressed his deep gratitude for all the support.",
        "synonyms": ["thankfulness", "appreciation", "gratefulness", "acknowledgment"],
        "antonyms": ["ungratefulness", "ingratitude", "thanklessness"],
        "rhymes": ["attitude", "latitude", "platitude"]
    },
    "resilience": {
        "hindi": "लचीलापन / पुनः संभलने की क्षमता",
        "hinglish": "Lachilapan / Punah Sambhalne Ki Kshamta",
        "ipa": "rɪˈzɪlɪəns",
        "pos": "noun",
        "definition": "The capacity to recover quickly from difficulties; toughness.",
        "example": "The community displayed remarkable resilience after the disaster.",
        "synonyms": ["toughness", "flexibility", "elasticity", "strength", "buoyancy"],
        "antonyms": ["fragility", "vulnerability", "weakness"],
        "rhymes": ["brilliance"]
    },
    "innovation": {
        "hindi": "नवीनता / नवाचार",
        "hinglish": "Naveenta / Navaachaar",
        "ipa": "ˌɪnəˈveɪʃən",
        "pos": "noun",
        "definition": "A new method, idea, product, or introducing new techniques.",
        "example": "Technological innovation is shaping the modern world.",
        "synonyms": ["invention", "novelty", "advancement", "creativity", "originality"],
        "antonyms": ["stagnation", "tradition", "outdatedness"],
        "rhymes": ["creation", "relation", "foundation"]
    },
    "compassion": {
        "hindi": "सहानुभूति / दया / करुणा",
        "hinglish": "Sahaanubhooti / Daya / Karuna",
        "ipa": "kəmˈpæʃən",
        "pos": "noun",
        "definition": "Sympathetic pity and concern for the sufferings or misfortunes of others.",
        "example": "He treated everyone with kindness and deep compassion.",
        "synonyms": ["empathy", "sympathy", "kindness", "benevolence", "tenderness"],
        "antonyms": ["cruelty", "callousness", "indifference", "harshness"],
        "rhymes": ["passion", "fashion"]
    },
    "curiosity": {
        "hindi": "जिज्ञासा / उत्सुकता",
        "hinglish": "Jigyaasa / Utsukta",
        "ipa": "ˌkjʊərɪˈɒsɪti",
        "pos": "noun",
        "definition": "A strong desire to know or learn something.",
        "example": "Curiosity drives scientific exploration and learning.",
        "synonyms": ["inquisitiveness", "interest", "eagerness", "wonder"],
        "antonyms": ["indifference", "disinterest", "apathy"],
        "rhymes": ["generosity", "animosity"]
    },
    "serenity": {
        "hindi": "शांति / स्थिरता",
        "hinglish": "Shaanti / Sthirta",
        "ipa": "sɪˈrɛnɪti",
        "pos": "noun",
        "definition": "The state of being calm, peaceful, and untroubled.",
        "example": "The mountain view brought an overwhelming sense of serenity.",
        "synonyms": ["peace", "calmness", "tranquility", "placidity", "stillness"],
        "antonyms": ["agitation", "chaos", "turmoil", "anxiety"],
        "rhymes": ["infinity", "affinity"]
    }
}


# ==============================================================================
# 5. MULTI-API LINGUISTIC & TRANSLATION ENGINE
# ==============================================================================

class LinguisticAPIClient:
    """Unified API client for high-performance translation, dictionary, and lexical research."""
    
    HEADERS = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
    }
    
    @classmethod
    def _http_get(cls, url: str, timeout: int = 5) -> Optional[Any]:
        """Makes an HTTP GET request and returns decoded JSON or None."""
        try:
            req = urllib.request.Request(url, headers=cls.HEADERS)
            with urllib.request.urlopen(req, timeout=timeout) as response:
                if response.status == 200:
                    raw_data = response.read().decode('utf-8')
                    return json.loads(raw_data)
        except Exception:
            return None
        return None

    @classmethod
    def translate_neural_endpoint(cls, text: str, src_lang: str = "en", tgt_lang: str = "hi") -> Optional[str]:
        """Fast neural translation endpoint for words, sentences, and paragraphs."""
        try:
            encoded = urllib.parse.quote(text.strip())
            url = f"https://clients5.google.com/translate_a/t?client=dict-chrome-ex&sl={src_lang}&tl={tgt_lang}&q={encoded}"
            req = urllib.request.Request(url, headers=cls.HEADERS)
            with urllib.request.urlopen(req, timeout=5) as res:
                data = json.loads(res.read().decode('utf-8'))
                if isinstance(data, list) and len(data) > 0:
                    if isinstance(data[0], str):
                        return data[0].strip()
                    elif isinstance(data[0], list) and len(data[0]) > 0:
                        return "".join([str(p[0]) for p in data[0] if p and len(p) > 0 and p[0]]).strip()
        except Exception:
            pass
        return None

    @classmethod
    def translate_mymemory(cls, text: str, src_lang: str = "en", tgt_lang: str = "hi") -> Dict[str, Any]:
        """Queries MyMemory API for alternative translations and confidence scores."""
        encoded_text = urllib.parse.quote(text.strip())
        url = f"https://api.mymemory.translated.net/get?q={encoded_text}&langpair={src_lang}|{tgt_lang}"
        data = cls._http_get(url, timeout=4)
        
        result = {
            "translated_text": "",
            "match_quality": 0,
            "alternatives": [],
            "source_lang": src_lang,
            "target_lang": tgt_lang,
            "success": False
        }
        
        if data and "responseData" in data:
            result["translated_text"] = data["responseData"].get("translatedText", "").strip()
            result["match_quality"] = data["responseData"].get("match", 0)
            result["success"] = bool(result["translated_text"])
            
            matches = data.get("matches", [])
            seen = set()
            if result["translated_text"]:
                seen.add(result["translated_text"].lower())
                
            for match in matches:
                trans = match.get("translation", "").strip()
                if trans and trans.lower() not in seen and len(trans) > 0:
                    seen.add(trans.lower())
                    result["alternatives"].append({
                        "text": trans,
                        "quality": match.get("quality", 0),
                        "subject": match.get("subject", "")
                    })
        return result

    @classmethod
    def translate(cls, text: str, src_lang: str = "en", tgt_lang: str = "hi") -> Dict[str, Any]:
        """Translates text bidirectionally using a resilient cascading strategy."""
        if not text or not text.strip():
            return {"translated_text": "", "success": False, "source_lang": src_lang, "target_lang": tgt_lang}
        
        clean_text = text.strip()
        primary_translation = cls.translate_neural_endpoint(clean_text, src_lang, tgt_lang)
        mymemory_res = cls.translate_mymemory(clean_text, src_lang, tgt_lang)
        
        final_text = primary_translation or mymemory_res.get("translated_text", "")
        
        # Offline fallback check
        if not final_text and src_lang == "en" and tgt_lang == "hi":
            clean_word = clean_text.lower()
            if clean_word in EMBEDDED_VOCABULARY_DATABASE:
                cached = EMBEDDED_VOCABULARY_DATABASE[clean_word]
                final_text = cached["hindi"]
                
        hinglish = ""
        if tgt_lang == "hi" and final_text:
            hinglish = HinglishTransliterator.transliterate(final_text)
            
        return {
            "translated_text": final_text,
            "hinglish": hinglish,
            "match_quality": mymemory_res.get("match_quality", 0.95 if primary_translation else 0),
            "alternatives": mymemory_res.get("alternatives", []),
            "source_lang": src_lang,
            "target_lang": tgt_lang,
            "success": bool(final_text)
        }

    @classmethod
    def fetch_dictionary_data(cls, word: str) -> Dict[str, Any]:
        """Queries Free Dictionary API for definitions, IPA phonetics, and usage examples."""
        encoded_word = urllib.parse.quote(word.strip().lower())
        url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{encoded_word}"
        data = cls._http_get(url, timeout=5)
        
        dict_info = {
            "phonetics": [],
            "ipa": "",
            "audio_url": "",
            "meanings": [],
            "source_urls": [],
            "found": False
        }
        
        if data and isinstance(data, list) and len(data) > 0:
            entry = data[0]
            dict_info["found"] = True
            
            for p in entry.get("phonetics", []):
                text_ipa = p.get("text", "")
                audio = p.get("audio", "")
                if text_ipa and not dict_info["ipa"]:
                    dict_info["ipa"] = text_ipa
                if audio and not dict_info["audio_url"]:
                    dict_info["audio_url"] = audio
                if text_ipa or audio:
                    dict_info["phonetics"].append({"ipa": text_ipa, "audio": audio})
                    
            if not dict_info["ipa"] and entry.get("phonetic"):
                dict_info["ipa"] = entry.get("phonetic")
                
            for m in entry.get("meanings", []):
                pos = m.get("partOfSpeech", "general")
                definitions_list = []
                synonyms_list = m.get("synonyms", [])
                antonyms_list = m.get("antonyms", [])
                
                for d in m.get("definitions", []):
                    def_text = d.get("definition", "")
                    example_text = d.get("example", "")
                    d_syn = d.get("synonyms", [])
                    d_ant = d.get("antonyms", [])
                    
                    if def_text:
                        definitions_list.append({
                            "definition": def_text,
                            "example": example_text,
                            "synonyms": d_syn,
                            "antonyms": d_ant
                        })
                
                dict_info["meanings"].append({
                    "part_of_speech": pos,
                    "definitions": definitions_list,
                    "synonyms": synonyms_list,
                    "antonyms": antonyms_list
                })
                
            dict_info["source_urls"] = entry.get("sourceUrls", [])
            
        return dict_info

    @classmethod
    def fetch_datamuse_relations(cls, word: str) -> Dict[str, List[str]]:
        """Fetches rich semantic lexical relations from Datamuse API."""
        clean_word = urllib.parse.quote(word.strip().lower())
        relations = {
            "synonyms": [],
            "antonyms": [],
            "rhymes": [],
            "associations": [],
            "describing_adjectives": []
        }
        
        endpoints = {
            "synonyms": f"https://api.datamuse.com/words?rel_syn={clean_word}&max=8",
            "antonyms": f"https://api.datamuse.com/words?rel_ant={clean_word}&max=8",
            "rhymes": f"https://api.datamuse.com/words?rel_rhy={clean_word}&max=8",
            "associations": f"https://api.datamuse.com/words?rel_trg={clean_word}&max=8",
            "describing_adjectives": f"https://api.datamuse.com/words?rel_jjb={clean_word}&max=8"
        }
        
        with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
            future_to_key = {
                executor.submit(cls._http_get, url, 4): key 
                for key, url in endpoints.items()
            }
            for future in concurrent.futures.as_completed(future_to_key):
                key = future_to_key[future]
                try:
                    res = future.result()
                    if res and isinstance(res, list):
                        relations[key] = [item["word"] for item in res if "word" in item]
                except Exception:
                    pass
                    
        return relations

    @classmethod
    def deep_word_research(cls, word: str) -> Dict[str, Any]:
        """
        Executes a multi-threaded deep research pipeline across all APIs
        combining translations, dictionary definitions, examples, relations, and Hinglish.
        """
        word = word.strip()
        report = {
            "word": word,
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
            "translation": {},
            "dictionary": {},
            "relations": {},
            "hinglish": "",
            "hindi_examples": [],
            "is_complete": False
        }
        
        with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
            future_trans = executor.submit(cls.translate, word, "en", "hi")
            future_dict = executor.submit(cls.fetch_dictionary_data, word)
            future_rel = executor.submit(cls.fetch_datamuse_relations, word)
            
            report["translation"] = future_trans.result()
            report["dictionary"] = future_dict.result()
            report["relations"] = future_rel.result()
            
        hindi_text = report["translation"].get("translated_text", "")
        if hindi_text:
            report["hinglish"] = HinglishTransliterator.transliterate(hindi_text)
            
        # Collect and translate real-world example sentences
        examples_to_translate = []
        if report["dictionary"]["found"]:
            for m in report["dictionary"]["meanings"]:
                for d in m["definitions"]:
                    if d.get("example") and len(examples_to_translate) < 2:
                        examples_to_translate.append(d["example"])
                        
        if not examples_to_translate and word.lower() in EMBEDDED_VOCABULARY_DATABASE:
            examples_to_translate.append(EMBEDDED_VOCABULARY_DATABASE[word.lower()]["example"])
            
        if examples_to_translate:
            with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
                future_examples = [executor.submit(cls.translate, ex, "en", "hi") for ex in examples_to_translate]
                for original_ex, f in zip(examples_to_translate, future_examples):
                    tr = f.result()
                    report["hindi_examples"].append({
                        "english": original_ex,
                        "hindi": tr.get("translated_text", ""),
                        "hinglish": tr.get("hinglish", "")
                    })
                    
        # Fallback to embedded dossier if online lookup had missing fields
        if not report["dictionary"]["found"] and word.lower() in EMBEDDED_VOCABULARY_DATABASE:
            offline = EMBEDDED_VOCABULARY_DATABASE[word.lower()]
            report["dictionary"]["found"] = True
            if not report["dictionary"].get("ipa") and offline.get("ipa"):
                report["dictionary"]["ipa"] = offline["ipa"]
            report["dictionary"]["meanings"].append({
                "part_of_speech": offline["pos"],
                "definitions": [{
                    "definition": offline["definition"],
                    "example": offline["example"],
                    "synonyms": offline["synonyms"],
                    "antonyms": offline["antonyms"]
                }],
                "synonyms": offline["synonyms"],
                "antonyms": offline["antonyms"]
            })
            for s in offline["synonyms"]:
                if s not in report["relations"]["synonyms"]:
                    report["relations"]["synonyms"].append(s)
            for a in offline["antonyms"]:
                if a not in report["relations"]["antonyms"]:
                    report["relations"]["antonyms"].append(a)
            for r in offline.get("rhymes", []):
                if r not in report["relations"]["rhymes"]:
                    report["relations"]["rhymes"].append(r)
                    
        report["is_complete"] = True
        return report


# ==============================================================================
# 6. SEARCH HISTORY, BOOKMARKS & DATA EXPORT MANAGER
# ==============================================================================

class ResearchHistoryManager:
    """Manages persistent history, bookmarks, and export capabilities."""
    
    FILE_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "translation_history.json")
    
    @classmethod
    def load_history(cls) -> List[Dict[str, Any]]:
        """Loads search history list from local JSON file."""
        if os.path.exists(cls.FILE_PATH):
            try:
                with open(cls.FILE_PATH, "r", encoding="utf-8") as f:
                    return json.load(f)
            except Exception:
                return []
        return []

    @classmethod
    def save_entry(cls, report: Dict[str, Any], is_favorite: bool = False):
        """Saves or updates an entry in the history store."""
        history = cls.load_history()
        word = report.get("word", "").strip()
        if not word:
            return
            
        fav = is_favorite
        for item in history:
            if item.get("word", "").lower() == word.lower() and item.get("favorite"):
                fav = True
                break

        entry = {
            "word": word,
            "hindi": report.get("translation", {}).get("translated_text", ""),
            "hinglish": report.get("hinglish", ""),
            "ipa": report.get("dictionary", {}).get("ipa", ""),
            "timestamp": report.get("timestamp", time.strftime("%Y-%m-%d %H:%M:%S")),
            "favorite": fav,
            "report": report
        }
        
        history = [h for h in history if h.get("word", "").lower() != word.lower()]
        history.insert(0, entry)
        history = history[:100]
        
        try:
            with open(cls.FILE_PATH, "w", encoding="utf-8") as f:
                json.dump(history, f, ensure_ascii=False, indent=2)
        except Exception:
            pass

    @classmethod
    def toggle_favorite(cls, word: str) -> bool:
        """Toggles the bookmark star on a word."""
        history = cls.load_history()
        status = False
        for item in history:
            if item.get("word", "").lower() == word.lower():
                item["favorite"] = not item.get("favorite", False)
                status = item["favorite"]
                break
        try:
            with open(cls.FILE_PATH, "w", encoding="utf-8") as f:
                json.dump(history, f, ensure_ascii=False, indent=2)
        except Exception:
            pass
        return status

    @classmethod
    def export_to_markdown(cls, file_path: str = "vocab_study_notes.md") -> str:
        """Exports history & vocabulary flashcards to a Markdown file."""
        history = cls.load_history()
        if not history:
            return "No history records to export."
            
        lines = [
            "# 📚 English to Hindi Linguistic Vocabulary Study Notes",
            f"Generated on: {time.strftime('%Y-%m-%d %H:%M:%S')}",
            f"Total Words: {len(history)}\n",
            "---",
        ]
        
        for item in history:
            word = item.get("word", "").capitalize()
            hindi = item.get("hindi", "")
            hinglish = item.get("hinglish", "")
            ipa = item.get("ipa", "")
            fav = "⭐ [STARRED]" if item.get("favorite") else ""
            
            lines.append(f"## 📖 {word} {fav}")
            lines.append(f"- **Hindi Translation**: `{hindi}` ({hinglish})")
            if ipa:
                lines.append(f"- **Phonetic (IPA)**: `/{ipa}/`")
                
            report = item.get("report", {})
            dict_data = report.get("dictionary", {})
            if dict_data and dict_data.get("meanings"):
                lines.append("\n### Definitions & Usage:")
                for m in dict_data["meanings"]:
                    pos = m.get("part_of_speech", "").upper()
                    lines.append(f"\n**[{pos}]**")
                    for d in m.get("definitions", []):
                        lines.append(f"- *Definition*: {d.get('definition', '')}")
                        if d.get("example"):
                            lines.append(f"  - *Example*: \"{d.get('example')}\"")
                            
            relations = report.get("relations", {})
            syns = relations.get("synonyms", [])
            ants = relations.get("antonyms", [])
            if syns:
                lines.append(f"- **Synonyms**: {', '.join(syns[:6])}")
            if ants:
                lines.append(f"- **Antonyms**: {', '.join(ants[:6])}")
                
            lines.append("\n---\n")
            
        full_path = os.path.abspath(file_path)
        with open(full_path, "w", encoding="utf-8") as f:
            f.write("\n".join(lines))
        return full_path

    @classmethod
    def export_to_csv(cls, file_path: str = "vocab_export.csv") -> str:
        """Exports vocabulary list to a spreadsheet CSV file."""
        history = cls.load_history()
        if not history:
            return "No history records to export."
            
        full_path = os.path.abspath(file_path)
        with open(full_path, "w", encoding="utf-8-sig", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Word", "Hindi Translation", "Hinglish Phonetics", "IPA", "Starred", "Timestamp"])
            for h in history:
                writer.writerow([
                    h.get("word", ""),
                    h.get("hindi", ""),
                    h.get("hinglish", ""),
                    h.get("ipa", ""),
                    "Yes" if h.get("favorite") else "No",
                    h.get("timestamp", "")
                ])
        return full_path


# ==============================================================================
# 7. INTERACTIVE TERMINAL UI (CLI)
# ==============================================================================

class TranslatorCLI:
    """Rich interactive command line interface."""
    
    @staticmethod
    def display_word_report(report: Dict[str, Any]):
        """Renders a structured word research report on console."""
        word = report.get("word", "").upper()
        trans = report.get("translation", {})
        hindi = trans.get("translated_text", "N/A")
        hinglish = report.get("hinglish", "")
        dict_data = report.get("dictionary", {})
        ipa = dict_data.get("ipa", "")
        relations = report.get("relations", {})
        
        print("\n" + "=" * 78)
        print(f"{Colors.BOLD}{Colors.CYAN} 🔍 LINGUISTIC RESEARCH REPORT: {Colors.YELLOW}{word}{Colors.RESET}")
        print("=" * 78)
        
        print(f"\n {Colors.BOLD}🇮🇳 Primary Hindi Translation:{Colors.RESET} {Colors.GREEN}{Colors.BOLD}{hindi}{Colors.RESET}")
        if hinglish:
            print(f" 🗣️  Hinglish Pronunciation:   {Colors.YELLOW}{hinglish}{Colors.RESET}")
        if ipa:
            print(f" 🎵 International Phonetics:  {Colors.MAGENTA}/{ipa}/{Colors.RESET}")
            
        audio_url = dict_data.get("audio_url", "")
        if audio_url:
            print(f" 🔊 Audio Pronunciation URL:  {Colors.DIM}{audio_url}{Colors.RESET}")

        alts = trans.get("alternatives", [])
        if alts:
            alt_texts = [f"{a['text']} ({a.get('quality', 0)}%)" for a in alts[:4]]
            print(f" 🔄 Alternative Meanings:     {Colors.CYAN}{', '.join(alt_texts)}{Colors.RESET}")

        if dict_data.get("found") and dict_data.get("meanings"):
            print(f"\n{Colors.BOLD}{Colors.WHITE} 📖 Grammatical Definitions & Parts of Speech:{Colors.RESET}")
            print(" " + "─" * 74)
            for m in dict_data["meanings"]:
                pos = m.get("part_of_speech", "").upper()
                print(f"  • {Colors.BOLD}{Colors.MAGENTA}[{pos}]{Colors.RESET}")
                for idx, d in enumerate(m.get("definitions", [])[:3], 1):
                    print(f"    {idx}. {Colors.WHITE}{d.get('definition', '')}{Colors.RESET}")
                    if d.get("example"):
                        print(f"       {Colors.ITALIC}{Colors.CYAN}Example:{Colors.RESET} \"{d.get('example')}\"")

        hindi_exs = report.get("hindi_examples", [])
        if hindi_exs:
            print(f"\n{Colors.BOLD}{Colors.WHITE} 💬 Contextual Bilingual Usage Sentences:{Colors.RESET}")
            print(" " + "─" * 74)
            for ex in hindi_exs:
                print(f"  🇬🇧 EN: {ex.get('english', '')}")
                print(f"  🇮🇳 HI: {Colors.GREEN}{ex.get('hindi', '')}{Colors.RESET} ({Colors.YELLOW}{ex.get('hinglish', '')}{Colors.RESET})\n")

        print(f"{Colors.BOLD}{Colors.WHITE} 🧠 Semantic & Lexical Associations:{Colors.RESET}")
        print(" " + "─" * 74)
        syns = relations.get("synonyms", [])
        ants = relations.get("antonyms", [])
        rhymes = relations.get("rhymes", [])
        collocs = relations.get("describing_adjectives", [])
        
        if syns:
            print(f"  ✨ {Colors.BOLD}Synonyms (समानार्थी):{Colors.RESET}  {Colors.GREEN}{', '.join(syns[:8])}{Colors.RESET}")
        if ants:
            print(f"  ⚡ {Colors.BOLD}Antonyms (विलोम):{Colors.RESET}      {Colors.RED}{', '.join(ants[:8])}{Colors.RESET}")
        if rhymes:
            print(f"  🎶 {Colors.BOLD}Rhyming Words:{Colors.RESET}        {Colors.MAGENTA}{', '.join(rhymes[:8])}{Colors.RESET}")
        if collocs:
            print(f"  🏷️  {Colors.BOLD}Common Adjectives:{Colors.RESET}    {Colors.CYAN}{', '.join(collocs[:8])}{Colors.RESET}")

        print("=" * 78 + "\n")

    @classmethod
    def run_deep_word_research(cls):
        """Interactively prompts user for a word and displays comprehensive linguistic research."""
        print(f"\n{Colors.BOLD}{Colors.CYAN}--- 🔍 DEEP WORD RESEARCH MODE ---{Colors.RESET}")
        word = input(f"{Colors.BOLD}Enter English word to analyze:{Colors.RESET} ").strip()
        if not word:
            print(f"{Colors.RED}No word entered.{Colors.RESET}")
            return
            
        print(f"\n{Colors.YELLOW}⏳ Contacting translation & linguistic knowledge APIs...{Colors.RESET}")
        report = LinguisticAPIClient.deep_word_research(word)
        ResearchHistoryManager.save_entry(report)
        cls.display_word_report(report)
        
        # Audio speech trigger
        AudioSpeechEngine.speak(word)
        
        fav_choice = input(f"⭐ Add {Colors.BOLD}{word}{Colors.RESET} to Starred Bookmarks? (y/n): ").strip().lower()
        if fav_choice.startswith('y'):
            ResearchHistoryManager.toggle_favorite(word)
            print(f"{Colors.GREEN}✓ Word saved to favorites!{Colors.RESET}")

    @classmethod
    def run_sentence_translation(cls):
        """Translates sentences or paragraphs with reverse translation support."""
        print(f"\n{Colors.BOLD}{Colors.CYAN}--- 📝 SENTENCE & PARAGRAPH TRANSLATOR ---{Colors.RESET}")
        print("1. English ➔ Hindi (अंग्रेज़ी से हिन्दी)")
        print("2. Hindi ➔ English (हिन्दी से अंग्रेज़ी)")
        direction = input(f"{Colors.BOLD}Select Direction (1 or 2, default=1):{Colors.RESET} ").strip()
        
        src_lang = "hi" if direction == "2" else "en"
        tgt_lang = "en" if direction == "2" else "hi"
        src_label = "Hindi" if src_lang == "hi" else "English"
        tgt_label = "English" if tgt_lang == "en" else "Hindi"
        
        print(f"\n{Colors.BOLD}Enter {src_label} text to translate:{Colors.RESET}")
        text = input("➔ ").strip()
        if not text:
            print(f"{Colors.RED}No text provided.{Colors.RESET}")
            return
            
        print(f"{Colors.YELLOW}⏳ Translating...{Colors.RESET}")
        res = LinguisticAPIClient.translate(text, src_lang, tgt_lang)
        
        print("\n" + "─" * 70)
        print(f"{Colors.BOLD}Original ({src_label}):{Colors.RESET}   {text}")
        print(f"{Colors.BOLD}Translation ({tgt_label}):{Colors.RESET} {Colors.GREEN}{Colors.BOLD}{res.get('translated_text', '')}{Colors.RESET}")
        if tgt_lang == "hi" and res.get("hinglish"):
            print(f"{Colors.BOLD}Hinglish / Phonetic:{Colors.RESET}     {Colors.YELLOW}{res.get('hinglish')}{Colors.RESET}")
        print("─" * 70 + "\n")

    @classmethod
    def run_vocabulary_quiz(cls):
        """Interactive Hindi-English Vocabulary Quiz game."""
        import random
        print(f"\n{Colors.BOLD}{Colors.MAGENTA}--- 🧠 HINDI-ENGLISH VOCABULARY QUIZ ---{Colors.RESET}")
        
        history = ResearchHistoryManager.load_history()
        vocab_pool = []
        for h in history:
            if h.get("word") and h.get("hindi"):
                vocab_pool.append({"word": h["word"], "hindi": h["hindi"], "hinglish": h.get("hinglish", "")})
                
        for k, v in EMBEDDED_VOCABULARY_DATABASE.items():
            if not any(x["word"].lower() == k.lower() for x in vocab_pool):
                vocab_pool.append({"word": k, "hindi": v["hindi"], "hinglish": v["hinglish"]})
                
        if len(vocab_pool) < 4:
            print(f"{Colors.YELLOW}Not enough vocabulary records yet. Please research a few words first!{Colors.RESET}")
            return
            
        rounds = min(5, len(vocab_pool))
        score = 0
        quiz_items = random.sample(vocab_pool, rounds)
        
        print(f"Starting {rounds}-question vocabulary challenge!\n")
        
        for idx, item in enumerate(quiz_items, 1):
            word = item["word"]
            correct_hindi = item["hindi"]
            
            other_options = [x["hindi"] for x in vocab_pool if x["word"] != word]
            if len(other_options) >= 3:
                distractors = random.sample(other_options, 3)
            else:
                distractors = ["सफलता", "आनंद", "प्रयास"]
                
            choices = [correct_hindi] + distractors
            random.shuffle(choices)
            correct_index = choices.index(correct_hindi) + 1
            
            print(f"{Colors.BOLD}Question {idx}/{rounds}:{Colors.RESET} What is the Hindi meaning of {Colors.YELLOW}{Colors.BOLD}'{word.upper()}'{Colors.RESET}?")
            for c_idx, choice in enumerate(choices, 1):
                print(f"  {c_idx}. {choice}")
                
            user_ans = input("Your answer (1-4): ").strip()
            if user_ans == str(correct_index):
                print(f"{Colors.GREEN}✓ Correct! शाबाश! {correct_hindi} ({item.get('hinglish', '')}){Colors.RESET}\n")
                score += 1
            else:
                print(f"{Colors.RED}✗ Incorrect. The correct answer was {correct_index}. {correct_hindi} ({item.get('hinglish', '')}){Colors.RESET}\n")
                
        print("=" * 40)
        print(f"🏆 Quiz Finished! Final Score: {Colors.BOLD}{score}/{rounds}{Colors.RESET}")
        percentage = (score / rounds) * 100
        if percentage >= 80:
            print(f"{Colors.GREEN}🌟 Outstanding vocabulary mastery!{Colors.RESET}")
        elif percentage >= 50:
            print(f"{Colors.YELLOW}👍 Good job! Keep practicing and researching words.{Colors.RESET}")
        else:
            print(f"{Colors.CYAN}💡 Keep learning with our Deep Word Research mode!{Colors.RESET}")
        print("=" * 40 + "\n")

    @classmethod
    def run_batch_research(cls):
        """Researches a list of comma-separated words in batch."""
        print(f"\n{Colors.BOLD}{Colors.CYAN}--- 📊 BATCH VOCABULARY RESEARCH & FLASHCARD BUILDER ---{Colors.RESET}")
        raw = input("Enter multiple English words separated by commas (e.g. empathy, grit, wisdom):\n➔ ").strip()
        if not raw:
            return
        words = [w.strip() for w in raw.split(",") if w.strip()]
        if not words:
            return
            
        print(f"\n{Colors.YELLOW}⏳ Researching {len(words)} words in parallel...{Colors.RESET}")
        
        with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
            future_to_word = {executor.submit(LinguisticAPIClient.deep_word_research, w): w for w in words}
            for future in concurrent.futures.as_completed(future_to_word):
                w = future_to_word[future]
                try:
                    rep = future.result()
                    ResearchHistoryManager.save_entry(rep)
                    hindi = rep.get("translation", {}).get("translated_text", "")
                    hinglish = rep.get("hinglish", "")
                    ipa = rep.get("dictionary", {}).get("ipa", "")
                    syns = ", ".join(rep.get("relations", {}).get("synonyms", [])[:4])
                    print(f"  ✓ {Colors.BOLD}{w.capitalize()}{Colors.RESET} ➔ {Colors.GREEN}{hindi}{Colors.RESET} ({hinglish}) | /{ipa}/ | Syns: {syns}")
                except Exception as e:
                    print(f"  ✗ {w}: Error {e}")
                    
        print(f"\n{Colors.GREEN}All {len(words)} words researched and saved to study history!{Colors.RESET}\n")

    @classmethod
    def run_view_history(cls):
        """Displays saved lookup history and starred vocabulary."""
        history = ResearchHistoryManager.load_history()
        print(f"\n{Colors.BOLD}{Colors.CYAN}--- 📜 SEARCH HISTORY & STARRED WORDS ({len(history)} entries) ---{Colors.RESET}")
        if not history:
            print("No search records yet. Research some words first!\n")
            return
            
        for idx, item in enumerate(history, 1):
            star = "⭐" if item.get("favorite") else "  "
            word = item.get("word", "").capitalize()
            hindi = item.get("hindi", "")
            hinglish = item.get("hinglish", "")
            ts = item.get("timestamp", "")
            print(f" {idx:2d}. {star} {Colors.BOLD}{word:<15}{Colors.RESET} ➔ {Colors.GREEN}{hindi:<20}{Colors.RESET} ({hinglish}) [{ts}]")
            
        print("\nCommands: (s <num>) Toggle Star | (e) Export Markdown | (c) Export CSV | (Enter) Back")
        cmd = input("Choice: ").strip()
        if cmd.startswith("s ") and len(cmd) > 2:
            try:
                sel_idx = int(cmd[2:]) - 1
                if 0 <= sel_idx < len(history):
                    w = history[sel_idx]["word"]
                    new_st = ResearchHistoryManager.toggle_favorite(w)
                    print(f"{'Starred' if new_st else 'Unstarred'} '{w}'.")
            except ValueError:
                pass
        elif cmd.lower() == "e":
            path = ResearchHistoryManager.export_to_markdown()
            print(f"{Colors.GREEN}Exported Markdown study notes to: {path}{Colors.RESET}")
        elif cmd.lower() == "c":
            path = ResearchHistoryManager.export_to_csv()
            print(f"{Colors.GREEN}Exported CSV spreadsheet to: {path}{Colors.RESET}")

    @classmethod
    def run_voice_speaker(cls):
        """Interactive voice speaker for words and sentences."""
        print(f"\n{Colors.BOLD}{Colors.CYAN}--- 🔊 NATIVE VOICE SPEAKER ---{Colors.RESET}")
        text = input("Enter English word or sentence to speak: ").strip()
        if text:
            print(f"{Colors.YELLOW}🔊 Speaking...{Colors.RESET}")
            AudioSpeechEngine.speak(text, is_async=False)

    @classmethod
    def main_loop(cls):
        """Main interactive menu loop for terminal mode."""
        print_banner()
        while True:
            print(f"\n{Colors.BOLD}📌 MAIN MENU - SELECT OPERATION:{Colors.RESET}")
            print(f" {Colors.CYAN}1.{Colors.RESET} 🔍 Deep Word Research (Meanings, Phonetics, POS, Synonyms & Antonyms)")
            print(f" {Colors.CYAN}2.{Colors.RESET} 📝 Sentence & Paragraph Translator (EN ➔ HI & HI ➔ EN)")
            print(f" {Colors.CYAN}3.{Colors.RESET} 📊 Batch Word Research & Flashcard Generator")
            print(f" {Colors.CYAN}4.{Colors.RESET} 🧠 Vocabulary Quiz Challenge Game")
            print(f" {Colors.CYAN}5.{Colors.RESET} 📜 View Search History & Starred Bookmarks")
            print(f" {Colors.CYAN}6.{Colors.RESET} 💾 Export Study Notes (Markdown / CSV)")
            print(f" {Colors.CYAN}7.{Colors.RESET} 🔊 Voice Audio Speaker (Text-to-Speech)")
            print(f" {Colors.CYAN}8.{Colors.RESET} 🖥️  Launch Graphical User Interface (GUI Studio)")
            print(f" {Colors.CYAN}9.{Colors.RESET} ❌ Exit Application")
            
            choice = input(f"\n{Colors.BOLD}Enter choice (1-9):{Colors.RESET} ").strip()
            
            if choice == "1":
                cls.run_deep_word_research()
            elif choice == "2":
                cls.run_sentence_translation()
            elif choice == "3":
                cls.run_batch_research()
            elif choice == "4":
                cls.run_vocabulary_quiz()
            elif choice == "5":
                cls.run_view_history()
            elif choice == "6":
                p_md = ResearchHistoryManager.export_to_markdown()
                p_csv = ResearchHistoryManager.export_to_csv()
                print(f"\n{Colors.GREEN}✓ Exported Study Notes to Markdown: {p_md}")
                print(f"✓ Exported Spreadsheet to CSV:       {p_csv}{Colors.RESET}\n")
            elif choice == "7":
                cls.run_voice_speaker()
            elif choice == "8":
                print(f"{Colors.CYAN}Launching Desktop GUI Studio...{Colors.RESET}")
                launch_gui()
            elif choice == "9" or choice.lower() in ("exit", "quit", "q"):
                print(f"\n{Colors.GREEN}धन्यवाद! Thank you for using English-Hindi Translator Studio. Goodbye!{Colors.RESET}\n")
                break
            else:
                print(f"{Colors.RED}Invalid option. Please choose between 1 and 9.{Colors.RESET}")


# ==============================================================================
# 8. MODERN DESKTOP GRAPHICAL USER INTERFACE (TKINTER STUDIO)
# ==============================================================================

def launch_gui():
    """Initializes and runs the Tkinter Desktop GUI Studio."""
    try:
        import tkinter as tk
        from tkinter import ttk, messagebox, scrolledtext
    except ImportError:
        print("Tkinter is not available in this environment. Running in CLI mode.")
        return

    root = tk.Tk()
    root.title("English ➔ Hindi Linguistic Translator & Word Research Studio")
    root.geometry("1020x720")
    root.minsize(850, 600)
    
    # Palette Theme
    BG_DARK = "#1e1e2e"
    BG_CARD = "#2a2b3d"
    BG_INPUT = "#313244"
    ACCENT_CYAN = "#89dceb"
    ACCENT_BLUE = "#89b4fa"
    ACCENT_GREEN = "#a6e3a1"
    ACCENT_YELLOW = "#f9e2af"
    ACCENT_MAGENTA = "#cba6f7"
    TEXT_MAIN = "#cdd6f4"
    TEXT_MUTED = "#a6adc8"
    
    root.configure(bg=BG_DARK)
    
    style = ttk.Style()
    style.theme_use('clam')
    
    style.configure("TNotebook", background=BG_DARK, borderwidth=0)
    style.configure("TNotebook.Tab", background=BG_CARD, foreground=TEXT_MAIN, padding=[16, 8], font=("Segoe UI", 10, "bold"))
    style.map("TNotebook.Tab", 
              background=[("selected", ACCENT_BLUE)], 
              foreground=[("selected", "#11111b")])
              
    style.configure("TFrame", background=BG_DARK)

    # Top Header Banner
    header_frame = tk.Frame(root, bg=BG_DARK, pady=10)
    header_frame.pack(fill="x", padx=20)
    
    title_lbl = tk.Label(header_frame, text="🌐 English ➔ Hindi Translation & Linguistic Studio", 
                         font=("Segoe UI", 16, "bold"), fg=ACCENT_CYAN, bg=BG_DARK)
    title_lbl.pack(anchor="w")
    
    subtitle_lbl = tk.Label(header_frame, text="Real-time multi-API translation, phonetics, parts of speech, synonyms, rhymes & vocabulary builder", 
                            font=("Segoe UI", 9), fg=TEXT_MUTED, bg=BG_DARK)
    subtitle_lbl.pack(anchor="w")

    # Main Notebook
    notebook = ttk.Notebook(root)
    notebook.pack(fill="both", expand=True, padx=20, pady=(0, 15))

    # --------------------------------------------------------------------------
    # TAB 1: 🔍 DEEP WORD RESEARCH STUDIO
    # --------------------------------------------------------------------------
    tab_research = ttk.Frame(notebook)
    notebook.add(tab_research, text="  🔍 Word Research Studio  ")
    
    search_bar = tk.Frame(tab_research, bg=BG_DARK, pady=8)
    search_bar.pack(fill="x")
    
    tk.Label(search_bar, text="English Word:", font=("Segoe UI", 11, "bold"), fg=TEXT_MAIN, bg=BG_DARK).pack(side="left", padx=(0, 10))
    
    word_entry = tk.Entry(search_bar, font=("Segoe UI", 12), bg=BG_INPUT, fg=TEXT_MAIN, insertbackground=TEXT_MAIN, relief="flat", width=25)
    word_entry.pack(side="left", ipady=4, padx=(0, 10))
    word_entry.insert(0, "perseverance")
    
    status_label = tk.Label(search_bar, text="", font=("Segoe UI", 9, "italic"), fg=ACCENT_YELLOW, bg=BG_DARK)
    status_label.pack(side="right", padx=10)

    # Result Card
    res_card = tk.Frame(tab_research, bg=BG_CARD, padx=15, pady=15)
    res_card.pack(fill="both", expand=True)

    summary_row = tk.Frame(res_card, bg=BG_CARD)
    summary_row.pack(fill="x", pady=(0, 10))
    
    word_title_lbl = tk.Label(summary_row, text="PERSEVERANCE", font=("Segoe UI", 15, "bold"), fg=ACCENT_YELLOW, bg=BG_CARD)
    word_title_lbl.pack(side="left")
    
    ipa_lbl = tk.Label(summary_row, text="", font=("Segoe UI", 12), fg=ACCENT_MAGENTA, bg=BG_CARD)
    ipa_lbl.pack(side="left", padx=10)
    
    hindi_trans_lbl = tk.Label(summary_row, text="", font=("Segoe UI", 16, "bold"), fg=ACCENT_GREEN, bg=BG_CARD)
    hindi_trans_lbl.pack(side="left", padx=15)
    
    hinglish_lbl = tk.Label(summary_row, text="", font=("Segoe UI", 12, "italic"), fg=ACCENT_CYAN, bg=BG_CARD)
    hinglish_lbl.pack(side="left")
    
    audio_holder = {"url": "", "word": "perseverance"}
    def play_voice():
        w = audio_holder["word"]
        AudioSpeechEngine.speak(w)
            
    audio_btn = tk.Button(summary_row, text="🔊 Speak Voice", command=play_voice, bg=BG_INPUT, fg=ACCENT_CYAN, font=("Segoe UI", 9, "bold"), relief="flat", padx=8)
    audio_btn.pack(side="right")
    
    star_btn = tk.Button(summary_row, text="☆ Bookmark", bg=BG_INPUT, fg=ACCENT_YELLOW, font=("Segoe UI", 9, "bold"), relief="flat", padx=8)
    star_btn.pack(side="right", padx=5)

    details_text = scrolledtext.ScrolledText(res_card, wrap="word", font=("Segoe UI", 10), bg=BG_INPUT, fg=TEXT_MAIN, insertbackground=TEXT_MAIN, relief="flat", padx=10, pady=10)
    details_text.pack(fill="both", expand=True)

    def do_research():
        w = word_entry.get().strip()
        if not w:
            return
        audio_holder["word"] = w
        status_label.config(text="⏳ Querying Linguistic APIs...")
        search_btn.config(state="disabled")
        
        def async_worker():
            rep = LinguisticAPIClient.deep_word_research(w)
            ResearchHistoryManager.save_entry(rep)
            
            def update_ui():
                status_label.config(text="✓ Research Complete")
                search_btn.config(state="normal")
                
                word_title_lbl.config(text=w.upper())
                hindi_val = rep.get("translation", {}).get("translated_text", "")
                hindi_trans_lbl.config(text=f"➔  {hindi_val}")
                hinglish_lbl.config(text=f"({rep.get('hinglish', '')})")
                
                ipa_val = rep.get("dictionary", {}).get("ipa", "")
                ipa_lbl.config(text=f" /{ipa_val}/" if ipa_val else "")
                
                audio_holder["url"] = rep.get("dictionary", {}).get("audio_url", "")
                
                details_text.delete("1.0", tk.END)
                
                # Definitions
                dict_d = rep.get("dictionary", {})
                if dict_d.get("meanings"):
                    details_text.insert(tk.END, "📖 GRAMMATICAL DEFINITIONS & PARTS OF SPEECH:\n", "heading")
                    details_text.insert(tk.END, "─" * 70 + "\n")
                    for m in dict_d["meanings"]:
                        pos = m.get("part_of_speech", "").upper()
                        details_text.insert(tk.END, f"• Part of Speech: [{pos}]\n", "pos")
                        for idx, d in enumerate(m.get("definitions", [])[:3], 1):
                            details_text.insert(tk.END, f"  {idx}. {d.get('definition', '')}\n")
                            if d.get("example"):
                                details_text.insert(tk.END, f"     Example: \"{d.get('example')}\"\n", "example")
                    details_text.insert(tk.END, "\n")
                    
                # Hindi Sentences
                hindi_ex = rep.get("hindi_examples", [])
                if hindi_ex:
                    details_text.insert(tk.END, "💬 BILINGUAL CONTEXTUAL USAGE:\n", "heading")
                    details_text.insert(tk.END, "─" * 70 + "\n")
                    for ex in hindi_ex:
                        details_text.insert(tk.END, f"  EN: {ex.get('english')}\n")
                        details_text.insert(tk.END, f"  HI: {ex.get('hindi')} ({ex.get('hinglish')})\n\n", "hindi_text")
                        
                # Semantic relations
                rel = rep.get("relations", {})
                details_text.insert(tk.END, "🧠 LEXICAL ASSOCIATIONS & VOCABULARY:\n", "heading")
                details_text.insert(tk.END, "─" * 70 + "\n")
                if rel.get("synonyms"):
                    details_text.insert(tk.END, f"  ✨ Synonyms (समानार्थी):  {', '.join(rel['synonyms'])}\n", "synonyms")
                if rel.get("antonyms"):
                    details_text.insert(tk.END, f"  ⚡ Antonyms (विलोम):      {', '.join(rel['antonyms'])}\n", "antonyms")
                if rel.get("rhymes"):
                    details_text.insert(tk.END, f"  🎶 Rhyming Words:        {', '.join(rel['rhymes'])}\n")
                if rel.get("describing_adjectives"):
                    details_text.insert(tk.END, f"  🏷️  Descriptive Words:    {', '.join(rel['describing_adjectives'])}\n")

                details_text.tag_config("heading", font=("Segoe UI", 10, "bold"), foreground=ACCENT_CYAN)
                details_text.tag_config("pos", font=("Segoe UI", 10, "bold"), foreground=ACCENT_MAGENTA)
                details_text.tag_config("example", font=("Segoe UI", 9, "italic"), foreground=ACCENT_YELLOW)
                details_text.tag_config("hindi_text", font=("Segoe UI", 10, "bold"), foreground=ACCENT_GREEN)
                details_text.tag_config("synonyms", foreground=ACCENT_GREEN)
                details_text.tag_config("antonyms", foreground="#f38ba8")
                
                def toggle_fav():
                    st = ResearchHistoryManager.toggle_favorite(w)
                    star_btn.config(text="⭐ Starred" if st else "☆ Bookmark")
                star_btn.config(command=toggle_fav, text="☆ Bookmark")
                
            root.after(0, update_ui)
            
        threading.Thread(target=async_worker, daemon=True).start()

    search_btn = tk.Button(search_bar, text="🔍 Deep Research", command=do_research, bg=ACCENT_BLUE, fg="#11111b", font=("Segoe UI", 10, "bold"), relief="flat", padx=12, pady=4)
    search_btn.pack(side="left")
    word_entry.bind("<Return>", lambda e: do_research())

    # --------------------------------------------------------------------------
    # TAB 2: 📝 SENTENCE TRANSLATOR
    # --------------------------------------------------------------------------
    tab_trans = ttk.Frame(notebook)
    notebook.add(tab_trans, text="  📝 Sentence Translator  ")
    
    trans_card = tk.Frame(tab_trans, bg=BG_CARD, padx=20, pady=20)
    trans_card.pack(fill="both", expand=True)

    ctrl_bar = tk.Frame(trans_card, bg=BG_CARD)
    ctrl_bar.pack(fill="x", pady=(0, 10))
    
    dir_label = tk.Label(ctrl_bar, text="Direction: English ➔ Hindi", font=("Segoe UI", 11, "bold"), fg=ACCENT_CYAN, bg=BG_CARD)
    dir_label.pack(side="left")
    
    current_direction = {"src": "en", "tgt": "hi"}
    def swap_direction():
        if current_direction["src"] == "en":
            current_direction["src"], current_direction["tgt"] = "hi", "en"
            dir_label.config(text="Direction: Hindi ➔ English")
            src_lbl.config(text="Input Hindi Text:")
            tgt_lbl.config(text="Translated English Text:")
        else:
            current_direction["src"], current_direction["tgt"] = "en", "hi"
            dir_label.config(text="Direction: English ➔ Hindi")
            src_lbl.config(text="Input English Text:")
            tgt_lbl.config(text="Translated Hindi Text:")
            
    swap_btn = tk.Button(ctrl_bar, text="⇄ Swap Direction", command=swap_direction, bg=BG_INPUT, fg=TEXT_MAIN, font=("Segoe UI", 9, "bold"), relief="flat", padx=10)
    swap_btn.pack(side="left", padx=15)

    boxes_frame = tk.Frame(trans_card, bg=BG_CARD)
    boxes_frame.pack(fill="both", expand=True)

    src_box_frame = tk.Frame(boxes_frame, bg=BG_CARD)
    src_box_frame.pack(side="left", fill="both", expand=True, padx=(0, 10))
    
    src_lbl = tk.Label(src_box_frame, text="Input English Text:", font=("Segoe UI", 10, "bold"), fg=TEXT_MAIN, bg=BG_CARD)
    src_lbl.pack(anchor="w", pady=(0, 5))
    
    src_text = scrolledtext.ScrolledText(src_box_frame, font=("Segoe UI", 11), bg=BG_INPUT, fg=TEXT_MAIN, insertbackground=TEXT_MAIN, relief="flat", height=12)
    src_text.pack(fill="both", expand=True)
    src_text.insert("1.0", "Knowledge and perseverance are the foundation of true success.")

    tgt_box_frame = tk.Frame(boxes_frame, bg=BG_CARD)
    tgt_box_frame.pack(side="right", fill="both", expand=True, padx=(10, 0))
    
    tgt_lbl = tk.Label(tgt_box_frame, text="Translated Hindi Text:", font=("Segoe UI", 10, "bold"), fg=TEXT_MAIN, bg=BG_CARD)
    tgt_lbl.pack(anchor="w", pady=(0, 5))
    
    tgt_text = scrolledtext.ScrolledText(tgt_box_frame, font=("Segoe UI", 11), bg=BG_INPUT, fg=ACCENT_GREEN, insertbackground=TEXT_MAIN, relief="flat", height=12)
    tgt_text.pack(fill="both", expand=True)

    bottom_row = tk.Frame(trans_card, bg=BG_CARD, pady=10)
    bottom_row.pack(fill="x")
    
    trans_status_lbl = tk.Label(bottom_row, text="", font=("Segoe UI", 9, "italic"), fg=ACCENT_YELLOW, bg=BG_CARD)
    trans_status_lbl.pack(side="left")

    def execute_sentence_translation():
        raw_val = src_text.get("1.0", tk.END).strip()
        if not raw_val:
            return
        trans_status_lbl.config(text="⏳ Translating...")
        
        def worker():
            res = LinguisticAPIClient.translate(raw_val, current_direction["src"], current_direction["tgt"])
            def ui_update():
                tgt_text.delete("1.0", tk.END)
                translated = res.get("translated_text", "")
                tgt_text.insert("1.0", translated)
                if current_direction["tgt"] == "hi" and res.get("hinglish"):
                    tgt_text.insert(tk.END, f"\n\n[Hinglish Pronunciation]:\n{res.get('hinglish')}")
                trans_status_lbl.config(text="✓ Translation Complete")
            root.after(0, ui_update)
            
        threading.Thread(target=worker, daemon=True).start()

    def speak_source():
        val = src_text.get("1.0", tk.END).strip()
        if val and current_direction["src"] == "en":
            AudioSpeechEngine.speak(val)

    speak_btn = tk.Button(bottom_row, text="🔊 Speak", command=speak_source, bg=BG_INPUT, fg=ACCENT_CYAN, font=("Segoe UI", 9, "bold"), relief="flat", padx=10, pady=4)
    speak_btn.pack(side="right", padx=(10, 0))

    translate_action_btn = tk.Button(bottom_row, text="⚡ Translate Now", command=execute_sentence_translation, bg=ACCENT_GREEN, fg="#11111b", font=("Segoe UI", 10, "bold"), relief="flat", padx=15, pady=5)
    translate_action_btn.pack(side="right")

    # --------------------------------------------------------------------------
    # TAB 3: 📜 HISTORY & STUDY EXPORT
    # --------------------------------------------------------------------------
    tab_hist = ttk.Frame(notebook)
    notebook.add(tab_hist, text="  📜 History & Study Notes  ")
    
    hist_card = tk.Frame(tab_hist, bg=BG_CARD, padx=20, pady=15)
    hist_card.pack(fill="both", expand=True)
    
    hist_toolbar = tk.Frame(hist_card, bg=BG_CARD)
    hist_toolbar.pack(fill="x", pady=(0, 10))
    
    tk.Label(hist_toolbar, text="Saved Vocabulary & Search History", font=("Segoe UI", 12, "bold"), fg=ACCENT_CYAN, bg=BG_CARD).pack(side="left")
    
    def refresh_history():
        hist_listbox.delete(0, tk.END)
        entries = ResearchHistoryManager.load_history()
        for idx, item in enumerate(entries, 1):
            star = "⭐ " if item.get("favorite") else "   "
            w = item.get("word", "").capitalize()
            hi = item.get("hindi", "")
            hgl = item.get("hinglish", "")
            ts = item.get("timestamp", "")
            hist_listbox.insert(tk.END, f"{star} {w:<18} ➔ {hi:<22} ({hgl})   [{ts}]")
            
    def export_md():
        p = ResearchHistoryManager.export_to_markdown()
        messagebox.showinfo("Export Successful", f"Exported study notes to Markdown:\n\n{p}")
        
    def export_csv_action():
        p = ResearchHistoryManager.export_to_csv()
        messagebox.showinfo("Export Successful", f"Exported vocabulary spreadsheet to CSV:\n\n{p}")

    tk.Button(hist_toolbar, text="🔄 Refresh", command=refresh_history, bg=BG_INPUT, fg=TEXT_MAIN, font=("Segoe UI", 9), relief="flat", padx=8).pack(side="right", padx=5)
    tk.Button(hist_toolbar, text="📊 Export CSV", command=export_csv_action, bg=BG_INPUT, fg=ACCENT_YELLOW, font=("Segoe UI", 9, "bold"), relief="flat", padx=8).pack(side="right", padx=5)
    tk.Button(hist_toolbar, text="📝 Export Markdown", command=export_md, bg=ACCENT_BLUE, fg="#11111b", font=("Segoe UI", 9, "bold"), relief="flat", padx=8).pack(side="right", padx=5)

    hist_listbox = tk.Listbox(hist_card, font=("Consolas", 10), bg=BG_INPUT, fg=TEXT_MAIN, selectbackground=ACCENT_BLUE, selectforeground="#11111b", relief="flat", height=15)
    hist_listbox.pack(fill="both", expand=True)

    def on_hist_double_click(event):
        sel = hist_listbox.curselection()
        if sel:
            entries = ResearchHistoryManager.load_history()
            if sel[0] < len(entries):
                w = entries[sel[0]].get("word", "")
                word_entry.delete(0, tk.END)
                word_entry.insert(0, w)
                notebook.select(0)
                do_research()
                
    hist_listbox.bind("<Double-Button-1>", on_hist_double_click)

    root.after(200, do_research)
    root.after(300, refresh_history)

    root.mainloop()


# ==============================================================================
# 9. CLI ENTRYPOINT & ARGUMENT PARSING
# ==============================================================================

def main():
    """Main application router."""
    parser = argparse.ArgumentParser(description="Advanced English to Hindi Translator & Linguistic Research Studio")
    parser.add_argument("--word", "-w", type=str, help="Research a specific English word directly")
    parser.add_argument("--translate", "-t", type=str, help="Translate a sentence or text directly")
    parser.add_argument("--speak", "-s", type=str, help="Speak text aloud using native text-to-speech")
    parser.add_argument("--src", type=str, default="en", help="Source language (default: en)")
    parser.add_argument("--tgt", type=str, default="hi", help="Target language (default: hi)")
    parser.add_argument("--gui", "-g", action="store_true", help="Launch Tkinter Desktop Graphical UI Studio directly")
    parser.add_argument("--export-md", type=str, nargs="?", const="vocab_study_notes.md", help="Export saved study notes to Markdown")
    parser.add_argument("--export-csv", type=str, nargs="?", const="vocab_export.csv", help="Export vocabulary list to CSV")
    
    args = parser.parse_args()
    
    if args.gui:
        launch_gui()
    elif args.speak:
        print(f"Speaking: '{args.speak}'...")
        AudioSpeechEngine.speak(args.speak, is_async=False)
    elif args.word:
        print_banner()
        print(f"\n{Colors.YELLOW}⏳ Contacting Linguistic APIs for '{args.word}'...{Colors.RESET}")
        rep = LinguisticAPIClient.deep_word_research(args.word)
        ResearchHistoryManager.save_entry(rep)
        TranslatorCLI.display_word_report(rep)
        AudioSpeechEngine.speak(args.word, is_async=False)
    elif args.translate:
        print_banner()
        res = LinguisticAPIClient.translate(args.translate, args.src, args.tgt)
        print("\n" + "─" * 70)
        print(f"Original ({args.src}):   {args.translate}")
        print(f"Translation ({args.tgt}): {Colors.GREEN}{Colors.BOLD}{res.get('translated_text', '')}{Colors.RESET}")
        if args.tgt == "hi" and res.get("hinglish"):
            print(f"Hinglish / Phonetic:     {Colors.YELLOW}{res.get('hinglish')}{Colors.RESET}")
        print("─" * 70 + "\n")
    elif args.export_md:
        p = ResearchHistoryManager.export_to_markdown(args.export_md)
        print(f"Exported study notes to: {p}")
    elif args.export_csv:
        p = ResearchHistoryManager.export_to_csv(args.export_csv)
        print(f"Exported CSV to: {p}")
    else:
        TranslatorCLI.main_loop()


if __name__ == "__main__":
    main()
