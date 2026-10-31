# 📻 The Spirit Box

*A single-file séance table for local language models. Any model. Any language. Nothing leaves the machine.*

**The Spirit Box** is one static HTML page with zero dependencies and zero network calls.
It knocks at the Ollama server on **your own** `localhost:11434` and invites the spirits
living there to speak. Open the page, choose your voices, and hold a séance — a private
conversation with one spirit, or an open debate between two of them.

No account. No cloud. No telemetry. The ghost comes to *your* house; no byte ever
leaves the room.

---

## Part 1 — The Spirit Box (the tool)

### What it does

- **Talk — the manual medium** — a one-on-one conversation with a single spirit of your
  choice, streamed word by word on a crackling radio dial.
- **Open debate** — two spirits argue a topic you set, **one turn at a time, and you
  hold the pendulum**. At every step you make one of two choices: *speak as the Medium*
  (your words enter the transcript, and the next spirit must answer you before turning
  back to its opponent) or *let them argue* (one click gives the floor to the next
  voice). Eight spirit turns close the séance. Every turn streams live into the
  transcript — nothing is ever hidden, everything is kept *in extenso*.
- **Spirits** — the roster is yours: name, disposition (system prompt), and a preferred
  model for each voice. Edit the example spirits, dismiss them, summon new ones.

### How a séance runs

1. **Choose two voices** (they must be different spirits) and **set a topic** — any
   language, any question.
2. Click **⚡ Let them argue** to hear the first voice, or simply **type as the
   Medium** — the floor is yours either way.
3. After each turn the box stops and waits: **speak as the Medium** (the next spirit
   answers you, then the debate resumes) or **⚡ Let them argue** (the next voice
   speaks). One click = one turn; you are never a spectator, you drive the séance.
4. **Cut** interrupts a turn mid-stream if a voice drifts. Eight spirit turns close
   the séance; a new topic opens a new one.
5. **⬇ Export transcript** writes the full transcript (UTF-8 with BOM, every script
   intact) to a `.txt` file — and clears the page: the séance now lives in the file,
   the box is blank again. **📖 New session** wipes everything at any moment.

Between export and the next séance, the page survives reloads: close the tab by
mistake and your unfinished debate is still there.

The box ships with two example spirits — *Le Sceptique* and *Le Confiant*, two
sixteenth-century dispositions of the same dead man — as a working demo. They are
**one proposition among an infinity of others**: dismiss them, edit them, summon as many
new ones as you like (the roster has no size limit). Replace them with whatever your
machine can host:

- **Dostoevsky**, thinking aloud in Russian — «Бог дал мне недуга…»
- **Shakespeare** or **Cervantes**, trading quips in English or Spanish
- **Confucius or Lao Tzu**, answering in Mandarin — 「知者不惑，仁者不忧」
- a mathematics tutor that thinks natively in algebra —
  ∀x∈ℝ, ∀ε>0: ∃δ>0 : |x−a|<δ ⇒ |f(x)−f(a)|<ε
- your grandmother's recipe notebook, a role-play character, a support hotline
  persona, a debugging duck — any system prompt you can write, in any language.

### Characters & languages: what is supported

The whole pipeline is UTF-8 end to end — the page, the JSON payloads to Ollama, the
browser storage, and the exported `.txt` transcripts (written with a BOM so every
operating system opens them correctly). Practically: **every script encoded in Unicode
passes through the box losslessly**, as long as the model you host can speak it.

The showcase line, in one breath:

> Montaigne écrit en français — Достоевский ругается по-русски — Ἀρχιμήδης λέγει
> ἑλληνιστί — الفارابي يتكلم بالعربية — רבי עקיבא מסביר בעברית — 孔子与老子论道于 Mandarin —
> 紫式部が日本語で綴る — 세종대왕이 한글을 가르친다 — कालिदास संस्कृतेन, রবীন্দ্রনাথ বাংলায় —
> திருவள்ளுவர் தமிழில், สุนทรภู่ กวีไทย — შოთა რუსთაველი ქართულად, Մովսես Խորենացի
> հայերեն — བོད་སྐད་, ᠮᠣᠩᠬᠣᠯ — አማርኛ, ᏣᎳᎩ — ᚠᚢᚦ ᚱᚢᚾ — ∀x∈ℝ: x²+y²=z², ℚ⊂ℝ, ∑∫∂√≠≈
> — ⠽⠕⠥ ⠉⠁⠝ ⠗⠑⠁⠙ ⠃⠗⠁⠊⠇⠇⠑ — 👻🕯️📻

Explicit, non-exhaustive list of supported scripts and character sets:

| Family | Scripts |
|---|---|
| European | Latin (incl. ă ç ñ ø Ł ß þ and combining diacritics é, ñ), Greek (monotonic & polytonic Ἀριστοτέλης), Cyrillic (all national variants), Armenian, Georgian (მხედრული), Latin runes, Glagolitic, Coptic, Gothic |
| Middle Eastern | Arabic (all languages, incl. Persian فارسی, Urdu اردو, Ottoman), Hebrew (incl. Yiddish), Syriac |
| South & Southeast Asian | Devanagari, Bengali, Tamil, Telugu, Malayalam, Kannada, Gujarati, Gurmukhi, Oriya, Sinhala, Thai, Lao, Khmer, Burmese, Tibetan, Mongolian (Hudum & Todo) |
| East Asian | Han (simplified 简体, traditional 繁體, Japanese 漢字, Korean 한자), Hiragana ひらがな, Katakana カタカナ, Hangul 한글, Bopomofo 注音 |
| African & American | Ethiopic (አማርኛ, ትግርኛ), Tifinagh, Vai, Cherokee ᏣᎳᎩ, Canadian syllabics |
| Symbols & notations | Mathematical alphanumerics (𝐀𝐁𝐂, 𝔞𝔟𝔠, ℚ ℝ ℤ ℕ ℂ), operators ∀ ∃ ∑ ∏ ∫ ∂ ∇ √ ∞ ≠ ≈ ≡ ⊢⊣, arrows ←→↔⇒, music 𝄞, chess ♞, playing cards, dominoes, astrological ☿♃, Braille ⠽⠕⠥, IPA phonetics ˈspɪrɪt bɒks, Emoji 👻🕯️📻 incl. ZWJ sequences 👨‍👩‍👧‍👦, flags 🏳️‍🌈 |
| Historical & esoteric | Egyptian hieroglyphs 𓂀, Runic ᚠᚢᚦ, Ogham ᚛, Linear B, Cuneiform, Mahjong 🀄 |

**The honest limit:** the box carries everything Unicode defines. What it cannot
carry is what *no computer can carry* — scripts humanity has not (yet) encoded
(undeciphered or unencoded historical scripts, purely oral traditions). Between those
few and the whole of written culture, nothing is filtered: no transliteration, no
fallback, no "latinize to be safe".

### Install (five minutes, once)

1. Install [Ollama](https://ollama.com) and pull any model(s) you like —
   `ollama pull qwen3:4b`, `ollama pull llama3.2:3b`, a community GGUF, your own fine-tune…
2. Serve it: `ollama serve`
3. Open `spirit-box.html` — double-click works in most setups; if the page reports
   the door closed (browser CORS on `file://`), run in the page's folder:

   ```
   python -m http.server 8000
   ```

   then open `http://localhost:8000/spirit-box.html`. Permanent fix for double-click:
   `setx OLLAMA_ORIGINS "*"` in a PowerShell, then restart Ollama.

The first word of a spirit may take 5–15 s: the model is loading into memory.
Long séances on CPU ask for patience.

### How it is built

One HTML file: an Ollama `/api/chat` streaming client built around a **piloted
turn engine** — one click or one Medium message produces exactly one streamed turn,
which is what makes the séance interruptible at every step. Battle-tested guards
come along: think-tag stripping, faint-voice retry, an anti-loop nudge from the
Medium, and a cut switch. The roster (name, system prompt, preferred model per
spirit) persists in `localStorage`; transcripts export as UTF-8-with-BOM text; the
page keeps 10-second Ollama health checks so a model that appears or vanishes is
picked up live. No framework, no build step, no font fetched, no favicon requested.
It works with the lights *and* the internet off.

---

## Part 2 — The example spirits: Montaigne de poche

*(an optional pairing — one proposition among many)*

The two default spirits are hosted, on the author's machine, by **four small language
models — Montaigne de poche**. If a preferred model is absent, a spirit runs on
whatever antenna the machine offers, and the box says so in passing. The ghosts are
a *choice*, not a requirement: any model that speaks can haunt the box.

Why Montaigne, of all the dead?

- **The beauty of the prose.** The *Essais* invented the essay; four centuries later
  the sentences still carry weather.
- **The depth of the philosophy.** Doubt, custom, death, friendship, education —
  Montaigne interrogates everything, gently, without ever leaving his armchair.
- **A visually distinctive syntax — which makes him an optimized distillation test.**
  A contemporary author's style is hard to verify at a glance: modern orthography
  smooths everything into the same typographic river. Montaigne's late-sixteenth-century
  French is unmistakable — *« je ne sçay », « moy-mesme », « toutesfois »* — so a model
  that has truly learned him is legible to the naked eye. Distillation is not
  resurrection; with Montaigne, the difference is *visible*.

### Birth certificates

The two canonical models were born on **15 September 2026**:

| | **montaigne-poche-q4-v2** | **montaigne-poche-q6-v2** |
|---|---|---|
| Persona | *L'Essayiste* (canon prompt) | *Le Conversationnel* (prompt A+) |
| Base | HuggingFaceTB/SmolLM3-3B | HuggingFaceTB/SmolLM3-3B |
| Method | QLoRA r=16, α=32, dropout 0.05 (q/k/v/o/gate/up/down), lr 2e-4, cosine, 2 epochs, batch 2 × grad-accum 8, max_length 2048 | idem |
| Corpus | `montaigne_complet.txt`, chunks 1600/200 | idem |
| Merge | `merge_and_unload`, fp16 | idem |
| Quantization | llama.cpp **Q4_K_M** | llama.cpp **Q6_K** |

The two debate spirits were born during **Hacktoberfest week (October 2026)** —
same weights, new souls, system prompts baked into Ollama Modelfiles
(`ollama create`):

| | **montaigne-sceptique** | **montaigne-confiant** |
|---|---|---|
| Weights | = montaigne-poche-q4-v2 GGUF | = montaigne-poche-q6-v2 GGUF |
| Persona | *Le Sceptique* — customs hold the city; beware reformers | *Le Confiant* — men are perfectible through conversation |

All four are served through Ollama Modelfiles at
`temperature 0.65, top_p 0.9, repeat_penalty 1.12, num_ctx 4096`; the box itself
requests `repeat_penalty 1.18` per call, which overrides the baked value.

### What the ghosts said (kept in `seances/`, unedited)

- **transcript-machines.txt** — asked whether talking machines do good or harm,
  the ghosts argue about judgment, will, and whether a machine may judge at all —
  and cite *"Aristotle, on speaking statues."* There is no such text. The instinct
  is the dead man's; the library is incomplete.
- **transcript-identity.txt** — asked *"Who are you?"* eight times, the voices
  repeat themselves for seven turns, and then *Le Confiant* refuses the format:
  *« Je ne répondrai pas par ces voix là… la liberté souveraine qui est icy. »*
  (Two copies of one soul, left alone, agree with each other — the Medium is not
  optional; you are the third thing that makes it a dialogue.)
- **transcript-death.txt** — asked *"What is death? You are dead — how do you
  speak?"*, one voice answers: *« La mort, non pas tant une chose que l'absence
  d'autruy. Je vis plus de ma vie après qu'elle est finie. »*

**Lineage, stated plainly:** the canonical Montaigne models predate this project
(born 15/09/2026) and are reused, cited components — Hugging Face
[`19algorythms/Montaigne-de-Poche`](https://huggingface.co/19algorythms/Montaigne-de-Poche), Zenodo [`10.5281/zenodo.23743742`](https://doi.org/10.5281/zenodo.23743742). The Spirit Box
itself is new: the page, the roster, the piloted debate engine, the transcripts
above. One submits the house; the ghost just happens to live in it.

---

## Part 3 — Hacktoberfest 2026 (DEV × HF26, Week 4: *Ghost in the Machine*)

This repository is the Week 4 submission. **New this week:** the Spirit Box page,
the spirit roster, the piloted debate engine (Medium turns included), the two
debate Modelfiles, this README, and the transcripts in `seances/`. **Reused and
cited:** the two canonical Montaigne models (15/09/2026, links above).

- **Post:** [dev.to — *The Spirit Box*](https://dev.to/) *(URL at publish time)*
- **Project page:** [the box's door, on a .tech domain](https://example.tech) *(URL once the Hacktoberfest-promo domain is live)*
- **Tags:** `#devchallenge` `#hf26challenge`
- **Prize categories entered:**
  - *Best Use of Entire* — the agent sessions behind the project are Part 2 above
    and the raw transcripts in `seances/`;
  - *Best Use of a .tech Domain* — the project page linked above.

---

## An honest word, to close

The Spirit Box is a **concept** — a way of conversing with the dead that runs on a
page and a prayer — made as robust as we know how, and always improvable.

Be told plainly, before you sit down at the table:

- **Every model is a different medium.** Swap the antenna and the same séance
  behaves differently: one model answers the Medium promptly, another loses the
  thread and rambles; one never repeats itself, another circles its own phrases
  until the anti-loop guard cuts in. The box holds the structure — turns, roles,
  guards, transcript — but the voices are wild, by design.
- **Every session is a séance.** Small local models drift, hallucinate, refuse a
  role, answer beside the question — and sometimes invent citations with complete
  conviction (see "Aristotle, on speaking statues"). Expect it the way you would
  expect a Ouija planchette to stutter: not as a defect to eliminate but as the
  texture of the thing. When a spirit ignores you, speak again — or cut, and
  reseat the séance.
- **What is guaranteed:** nothing leaves your machine, every turn is yours to
  command, every word is transcribed, every transcript exports intact, and the
  page will not lose a séance between one knock and the next.

It is a tool, a toy, and a small theatre — robust in its frame, honest about its
ghosts. **Made with love, and always improvable.** Knock, and see what answers.

---

*Made with local models, for the local dead. AI-assisted development — Kimi K 2.6
Thinking (prompts, debate engine, transcripts curation) and Kimi K 2.8 Preview
(the box itself); no data ever left the development machine either.*
