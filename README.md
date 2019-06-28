# IR-Spectra
#### Created by [Victoria Catlett](https://github.com/vcatlett) and [Miguel Gutierrez](https://github.com/mgutierrez32)

These scripts display high-resolution near-infrared spectra from the University of Texas at Austin's [Immersion Grating Infrared Spectrometer](https://www.as.utexas.edu/astronomy/research/people/jaffe/igrins.html) (IGRINS).

[Create_File_List.py](Create_File_List.py) makes a list of all of the files you want [IGRINS_Spectrum_Viewer.py](IGRINS_Spectrum_Viewer.py) to use. 

[IGRINS_Spectrum_Viewer.py](IGRINS_Spectrum_Viewer.py) creates an interactive environment for viewing spectra from IGRINS. The left and right arrow keys scroll through different orders in a file, the up and down arrow keys change the file, and the spacebar changes the band. 

## Getting Started

Make sure all of your data is in the same directory. Then, replace 'Your/Path/Name/' in both [Create_File_List.py](Create_File_List.py) (line 7) and [IGRINS_Spectrum_Viewer.py](IGRINS_Spectrum_Viewer.py) (line 123) with the path to that folder. 

Run [Create_File_List.py](Create_File_List.py) to make a list of file names for [IGRINS_Spectrum_Viewer.py](IGRINS_Spectrum_Viewer.py) to read. It should save in the same directory as the files themselves. 

[IGRINS_Spectrum_Viewer.py](IGRINS_Spectrum_Viewer.py) requires the data to be .fits files. The expected extensions are

| No. | Name |
|-----|----------|
| 0 | SPEC_COMBINED | 
| 1 | WAVELENGTH |
| 2 | UNC_FLUX |
| 3 | SNR |

If these are not the extensions of your data, the numbers can be edited in lines 15-17. 

## Required Packages

These scripts require os, numpy, astropy, and matplotlib.
