# PERFEC System Development Blueprint & Workflow

This document outlines the architectural constraints and communication workflow for developing new hardware components for the PERFEC System MIDI project on the Circuit Playground Express (SAMD21).

---

## 1. Core Architectural Constraints
To maintain microsecond-level timing accuracy and prevent `MemoryError` crashes on the SAMD21 chip, all new code must adhere to these strict performance rules:

* **Zero-Allocation Execution**: No dynamic object instantiation (`[ ]`, `{ }`, `bytes([x])`, string formatting) inside active execution loops. All data shapes must be pre-allocated in memory at boot.
* **Pre-Cached Methods**: Bound methods (e.g., `self.midi.get_msg`) must be resolved once during initialization or micro-cached locally immediately before entering the `while True:` loop.
* **No Software-Emulated Floats**: Use pure integer math (`//`) instead of floating-point math (`/`) to save CPU cycles on the FPU-less SAMD21 processor.
* **No `isinstance()` or Modulo (`%`) Operations**: Replace `isinstance()` with class type identity checks (`.__class__ is ClassName`), and replace `%` with boundary rollover conditions (`if idx >= LIMIT: idx = 0`).
* **Controlled Garbage Collection**: Keep global garbage collection enabled, but manually invoke `gc.collect()` *only* at non-time-critical junctions (e.g., on the downbeat after MIDI pulses have successfully fired).

---

## 2. Future AI Prompt Template
When starting a new development session with an AI assistant to build a new component, copy and paste the text block below into the first prompt to instantly align the context boundary:

```text
We are building a new component for the PERFEC System MIDI project on the Circuit Playground Express (SAMD21). The system architecture uses a zero-allocation, micro-cached, straight-time paradigm to prevent timing jitter and MemoryErrors. Do not use float math, string-based messaging, or dynamic object instantiation inside execution loops. Let's start by designing the architecture for [INSERT NEW COMPONENT NAME HERE].
```

---

## 3. Step-by-Step Development Workflow
To prevent code regression, expand the codebase module-by-module in this specific order:

### Step 1: The Model (`model.py`)
Establish or modify the underlying application state data first. 
* Add new state trackers as integers or fixed-size lists inside the model's `__init__`.
* Pre-calculate array or tuple lengths at startup to eliminate runtime `len()` overhead.
* Write localized mutation methods that change attributes without altering object identities.

### Step 2: The View & Input Hardware (`board_controller.py` / `cpx.py`)
Wire up physical IO interactions to match the updated model changes.
* Map physical button debouncers or switches directly using high-speed lambda expressions or local reference pointers.
* Flatten any visual update code (like NeoPixel manipulation loops) to write color values directly to array indices, entirely bypassing multi-layered parent `super()` calls or color helper function stacks.

### Step 3: The System Main Loop (`code.py`)
Integrate the fully complete model and view components together.
* Pre-instantiate all potential application views once at startup to avoid runtime object destruction and reallocation.
* Map structural states using dictionary key-lookups instead of branching `if/elif` logic statements.
* Use a single local tracking assignment for time collection references (like passing a pre-fetched `time.monotonic_ns()` down through your time check parameters).

### Step 4: Component Review
When updating an existing module, provide only the target **class block or isolated function loop** to the assistant rather than pasting the entire codebase file. This prevents the LLM from truncating code or accidentally rolling back existing micro-caches.
