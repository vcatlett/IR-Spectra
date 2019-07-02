# IR-Spectra
#### Created by [Victoria Catlett](https://github.com/vcatlett) and [Miguel Gutierrez](https://github.com/mgutierrez32)

These scripts display high-resolution near-infrared spectra from the University of Texas at Austin's [Immersion Grating Infrared Spectrometer](https://www.as.utexas.edu/astronomy/research/people/jaffe/igrins.html) (IGRINS).

* [Create_File_List.py](Create_File_List.py) makes a list of all of the files that [IGRINS_Spectrum_Viewer.py](IGRINS_Spectrum_Viewer.py) will use. 

* [IGRINS_Spectrum_Viewer.py](IGRINS_Spectrum_Viewer.py) creates an interactive environment for viewing spectra from IGRINS. The left and right arrow keys scroll through different orders in a file, the up and down arrow keys change the file, and the spacebar changes the band. 

## Getting Started

Make sure all of your data is in the same directory. Then, replace ```'/Your/Path/Name/'``` in both line 7 of [Create_File_List.py](Create_File_List.py) and line 121 of [IGRINS_Spectrum_Viewer.py](IGRINS_Spectrum_Viewer.py) with the path to that directory. 

Your files must start with ```'SDCH'``` and ```'SDCK'``` or they must end with ```'H.fits'``` and ```'K.fits'```, otherwise you will need to adjust lines 13 and 15 of [Create_File_List.py](Create_File_List.py) accordingly. Run the script to make a list of file names that [IGRINS_Spectrum_Viewer.py](IGRINS_Spectrum_Viewer.py) can read. It should save in the same directory as the files themselves. 

[IGRINS_Spectrum_Viewer.py](IGRINS_Spectrum_Viewer.py) requires the data to be ```fits``` files. It expects the extensions

| No. | Name |
|:-----:|:----------:|
| 0 | SPEC_DIVIDE_A0V | 
| 1 | WAVELENGTH |
| 2 | TGT_SPEC |
| 3 | A0V_SPEC |
| 4 | VEGA_SPEC |
| 5 | SNR |

This script plots the wavelengths (extension 1, converted to velocity space) against the adjusted flux (extension 0) in the top subplot and against the spectrum of a nearby A0V star (extension 3) in the bottom subplot. If these are not the extensions of your data, the numbers can be edited in lines 15-17. Extension 5, the signal-to-noise ratio, may not be present in all data, so it is not used in the script. 

## Required Packages

These scripts require os, numpy, astropy, and matplotlib.

## Acknowledgements

Our project is supported by the "[Frontier Research and Training in Astronomy for the 21st Century](https://astronomy.utexas.edu/research/astronomy-reu-assure)" program and the [TAURUS](https://sites.cns.utexas.edu/taurus/home) program through UT Austin's Department of Astronomy and the McDonald Observatory. We are under the guidance of [Ben Tofflemire](https://github.com/tofflemire), a postdoctoral researcher in UT Austin's Department of Astronomy. 
