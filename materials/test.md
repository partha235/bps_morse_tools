The standard Morse code prosign to **invite the other station to transmit** (i.e., to start or hand over the conversation) is:

**K**  
−·−

Meaning: “Go ahead, transmit” / “Over”  

### Common related prosigns you’ll hear at the start/end of exchanges:

- **K** (−·−) → General “over” / invite anyone to reply  
- **AR** (·−·−·) → “End of message, over” (often used instead of K when the message is finished)  
- **KN** (−·−−·) → “Over, only the station I’m talking to should reply” (more specific than K)  
- **SK** (···−·−) or **VA** → “End of contact” / “goodbye”  
- **CL** (−·−··−··) → “Closing down / going off air”

So when you’re ready for the other person to start talking or reply, you just send:

**−·−** (K)

Example of a very simple QSO start:  
CQ CQ CQ DE [your call] [your call] K  
(−−·−· −−·−· −−·−· ···· −·· ·   [your call twice]   −·−)

That final K means “calling all stations, please come back to me.”

---


For Morse code speed, **WPM (Words Per Minute)** is usually based on the standard word **“PARIS”** which equals **50 dot units**.

This concept is part of the Morse timing standard used in Morse Code.

---

## Step 1: Calculate dot duration

Formula:

$
\text{dot time} = \frac{1200}{WPM} \text{ ms}
$

For **8 WPM**:

$
\frac{1200}{8} = 150 \text{ ms}
$
So:

* **Dot = 150 ms**
* **Dash = 450 ms**
* **Space between symbols = 150 ms**
* **Space between letters = 450 ms**

---

## Step 2: Letters per second

Standard word **PARIS = 5 letters**

At **8 WPM**:

$
8 \text{ words/min} \times 5 = 40 \text{ letters/min}
$

Convert to seconds:

$
40 / 60 = 0.67 \text{ letters/sec}
$

---

✅ **Final result**

At **8 WPM ≈ 0.67 alphabet per second**

or

* **1 letter every ~1.5 seconds**

---

## Quick reference

| WPM | Letters/sec |
| --- | ----------- |
| 5   | 0.42        |
| 8   | 0.67        |
| 10  | 0.83        |
| 12  | 1           |
| 20  | 1.67        |

---

💡 Since you are generating random letters with `espeak`, if you want **true 8 WPM timing**, the delay should be around:

```python
sleep(1.5)
```

instead of `0.5`.

---

If you want, I can also show you a **Python Morse trainer that automatically adjusts timing for any WPM (5–40 WPM)**. It’s very useful if you're practicing decoding.
