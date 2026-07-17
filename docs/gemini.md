# Context for Continued Development: PERFEC Modular MIDI Suite

We are developing a modular MIDI clock and sequencer suite running on Adafruit Circuit Playground Express (CPX) boards (SAMD21 processor) under CircuitPython. The suite connects to a hardware/Pico 2W master clock and test rig.

This codebase serves as a teaching tool for high school computer science students. The goal is to maximize real-time timing execution and eliminate latency jitter while reinforcing structural computing principles.

## 1. System Aims & Critical Timing Constraints
* **Zero Runtime Heap Allocation:** Tight timing loops running thousands of times per second must NOT create dynamic objects (no dynamic strings, no dynamic dictionary generations, no list slicing `[:]`, no raw byte allocations like `bytes([msg])`, and no local `range()` definitions inside `while` blocks). 
* **Prevent "MIDI Choke":** Avoid duplicate state messages on the wire. For example, do not stream out redundant `NoteOff` messages on empty rhythm steps; only issue a `NoteOff` if an active `NoteOn` was intentionally fired on that step.
* **Proactive Memory Management:** Automatic background reactive garbage collection must be disabled at boot (`gc.disable()`). Micro-sweeps (`gc.collect()`) are explicitly triggered only during safe, low-priority timing windows (like right after a clock tick finishes processing).
* **Latency Compensation:** Account for blocking hardware tasks (like NeoPixel updates or slide switch pin polling) by pre-calculating fixed latency buffers (`config.latency_ns`) and utilizing timeline-anchored timestamps (`next_pulse = now + ns_per_pulse`).

## 2. Programming Style & Educational Goals
* **Reinforce Low-Level Concepts:** Maintain literal representations for hexadecimal values (e.g., status bytes like `b'\xF8'`) and binary forms (e.g., masks like `0b10000000`). Do not abstract these away into arbitrary integers.
* **Readability Over Complex Python Tricks:** Avoid overly advanced or dense syntax shorthand (such as inline ternary statements: `x = 1 if condition else 0`). Prioritize clear, standard, nested block structures (`if/else`) that high school students can easily trace, read, and modify.
* **Preserve Documentation:** Retain all original multi-line docstrings, inline comments, variable descriptions, and copyright/licensing headers.
* **Type Hinting:** Maintain explicit type hints on all variables, argument signatures, and method return parameters (e.g., `def main(self) -> "View":`).

## 3. Core Structural Patterns
* **Micro-Caching Buffer Patterns:** Pre-allocate static, mutable objects (like a 3-byte `bytearray` for note outputs or a 1-byte `bytearray` paired with `.readinto()` for MIDI ingestion) inside object constructors (`__init__`) to overwrite data allocation-free at runtime.
* **Bresenham Integer Math:** Avoid float operations and floating-point round-off errors. Use integer-only accumulator loops to spacing pulses or scale percentages (e.g., `(PPQN * ratio) // 100`).
* **Object-Oriented 2D State Machines:** Split system modes (Playing, Stopped, Config) into cleanly isolated View and Controller classes. 
* **Type-Mapped Dictionary Routing:** Avoid runtime reflection checks (like `isinstance()`) or chain-nested `if/elif` statements in the main execution thread. Look up and swap active class instances using static, pre-allocated dictionary maps indexed by class types or switch booleans (e.g., `view_map[switch_state][type(mc)]`).

## Instructions for the AI Assistant:
When helping to expand, troubleshoot, or add new modules to this suite:
1. Ensure all code modifications perfectly match the zero-allocation and performance rules laid out above.
2. Structure new feature blocks to highlight an educational takeaway (e.g., bit shifting, binary interpretation, indexing math).
3. Do not over-complicate or optimize beyond the physical constraints of the 10-LED CPX hardware bar if it yields diminishing returns for readability.
4. Output complete, updated files when requested to make pasting to the board drive straightforward.
