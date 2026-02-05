# Short Answers (Lecture-2)

## Q1
**What is the difference between time domain and frequency domain?**  
Time domain shows how a signal changes over time (amplitude vs. time). Frequency domain shows the frequencies that make up the signal (magnitude vs. frequency). In the time domain, we observe the waveform shape, while in the frequency domain we see peaks that represent the strength of each frequency component.

## Q2
**Why does filtering help in RF receivers?**  
Filtering helps an RF receiver select the desired signal while removing unwanted signals and noise. It reduces interference from nearby channels and improves signal quality, making the signal easier to process and demodulate.

## Q3
**What does modulation achieve in an RF system?**  
Modulation shifts a low-frequency baseband signal onto a high-frequency carrier for efficient transmission. This allows signals to travel longer distances, supports smaller antennas, and enables multiple signals to share the same communication medium using different carrier frequencies.

## Q4
**From A2: which filter was easiest to design and why?**  
The low-pass filter (LPF) or high-pass filter (HPF) was the easiest to design because only one cutoff frequency is required. For example, setting a cutoff between 500 Hz and 600 Hz allows the LPF to keep the 500 Hz component while removing higher frequencies. Band-pass filters require two cutoff points, making them slightly more complex.

## Q5
**From A3: where do the new frequency components appear after modulation?**  
After modulation, new frequency components appear at **fc − fm** and **fc + fm**. With a carrier frequency of 2000 Hz and a message frequency of 100 Hz, the peaks occur at approximately **1900 Hz** and **2100 Hz**.
