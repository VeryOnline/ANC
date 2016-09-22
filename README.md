#	ANC
A little project on software driven active noise cancellation. Very newly started. The basic idea is to record
ambient noise, generate the corresponding anti-waveform and play it through the earphones. This project is intended 
to facilitate learning Python. 

## Stuff done
* IO object for reading and writing from internal objects, text and bytes.
* Tests for IO func.
* Some list manipulation tools.
* Added sounddevice library and dependencies to capture bytes from sound card
* Added sample scripts on reading and writing to sound device, block read and write for now, will use callback function later.

## To do
* Figure out how to write to sound device (urgent)
* Test for list manipulation tools
* Look into FFT and implementation (do way later)