#pylint: disable=trailing-whitespace, line-too-long, bad-whitespace, invalid-name, R0204, C0200
#pylint: disable=superfluous-parens, missing-docstring, broad-except
#pylint: disable=too-many-lines, too-many-instance-attributes, too-many-statements, too-many-nested-blocks
#pylint: disable=too-many-branches, too-many-public-methods, too-many-locals, too-many-arguments

#============================================================================
#RF Explorer Python Libraries - A Spectrum Analyzer for everyone!
#Copyright © 2010-16 Ariel Rocholl, www.rf-explorer.com
#
#This application is free software; you can redistribute it and/or
#modify it under the terms of the GNU Lesser General Public
#License as published by the Free Software Foundation; either
#version 3.0 of the License, or (at your option) any later version.
#
#This software is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
#General Public License for more details.
#
#You should have received a copy of the GNU General Public
#License along with this library; if not, write to the Free Software
#Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
#=============================================================================

from ctypes import c_int8

class RFE6GEN_CalibrationData:
    """note this is shared with RFEGenTest
    """
    def __init__(self):
        #actual -30dBm adjusted values read from signal generator
        self.m_arrSignalGeneratorEmbeddedCalibrationActual30DBM = None #-30dBm

        self.m_arrSignalGeneratorCalRanges_KHZ = [
            25000, 33000, 41000, 49000, 57000, 65000, 73000, 81000,
            89000, 97000, 100000, 116000, 132000, 148000, 164000, 180000,
            196000, 212000, 228000, 244000, 260000, 276000, 292000, 308000,
            324000, 340000, 356000, 372000, 388000, 404000, 420000, 436000,
            452000, 468000, 484000, 500000, 532000, 564000, 596000,
            628000, 660000, 692000, 724000, 756000, 788000, 820000, 852000,
            884000, 916000, 948000, 980000, 1012000, 1044000, 1076000, 1108000,
            1140000, 1172000, 1204000, 1236000, 1268000, 1300000, 1332000, 1364000,
            1396000, 1428000, 1460000, 1492000, 1524000, 1556000, 1588000, 1620000,
            1652000, 1684000, 1716000, 1748000, 1780000, 1812000, 1844000, 1876000,
            1908000, 1940000, 1972000, 2004000, 2036000, 2068000, 2100000, 2132000,
            2164000, 2196000, 2228000, 2260000, 2292000, 2324000, 2356000, 2388000,
            2420000, 2452000, 2484000, 2516000, 2548000, 2580000, 2612000, 2644000,
            2676000, 2708000, 2740000, 2772000, 2804000, 2836000, 2868000, 2900000,
            2932000, 2964000, 2996000, 3000000, 3064000, 3128000, 3192000, 3256000,
            3320000, 3384000, 3448000, 3512000, 3576000, 3640000, 3704000, 3768000,
            3832000, 3896000, 3960000, 4024000, 4088000, 4152000, 4216000, 4280000,
            4344000, 4408000, 4472000, 4536000, 4600000, 4664000, 4728000, 4792000,
            4856000, 4920000, 4984000, 5048000, 5112000, 5176000, 5240000, 5304000,
            5368000, 5432000, 5496000, 5560000, 5624000, 5688000, 5752000, 5816000,
            5880000, 5944000]

        #pre-defined const values for different power level configurations organized as {L2,L1,L0,H3,H2,H1,H0}
        self.m_arrDeltaAmplitude = [
            [-3.23,	-6.24,	 -9.29,	  29.72,   26.71,	23.62,	 20.68],
            [-3.22,	-6.25,	 -9.25,	  29.76,   26.85,	23.81,	 20.77],
            [-3.23,  -6.25,   -9.26 ,  29.89,   26.73,   23.79,   20.78],
            [-3.24,  -6.29,   -10.71,  29.87,   26.82,   23.7 ,   20.82],
            [-3.23,  -6.28,   -9.2  ,  30.01,   26.9 ,   23.87,   20.78],
            [-3.24,  -6.3 ,   -10.69,  29.98,   26.85,   23.89,   20.88],
            [-3.27,  -6.31,   -9.3  ,  30.07,   26.97,   23.97,   20.91],
            [-3.26,  -6.31,   -9.37 ,  30.02,   26.95,   23.91,   20.83],
            [-3.26,  -6.33,   -9.35 ,  29.98,   27.03,   23.98,   20.97],
            [-3.25,  -6.34,   -9.37 ,  30.06,   26.92,   22.67,   19.48],
            [-3.26,  -6.34,   -10.75,  30.11,   27.01,   23.89,   20.95],
            [-3.26,  -6.31,   -9.38 ,  30.22,   27.02,   23.98,   20.88],
            [-3.24,  -6.31,   -9.32 ,  30.2 ,   27.06,   23.97,   19.51],
            [-3.34,  -6.34,   -9.36 ,  30.15,   26.92,   23.79,   20.98],
            [-3.27,  -6.39,   -9.36 ,  30.31,   27.02,   23.96,   20.89],
            [-3.35,  -6.43,   -9.49 ,  30.26,   26.98,   23.92,   20.9 ],
            [-3.27,  -6.37,   -9.4  ,  30.33,   27.05,   23.98,   20.95],
            [-3.25,  -6.38,   -9.32 ,  30.37,   27.09,   24.02,   20.94],
            [-3.33,  -6.4 ,   -9.39 ,  30.25,   25.82,   23.91,   20.82],
            [-3.27,  -6.3 ,   -9.36 ,  30.27,   27.01,   23.98,   20.94],
            [-3.29,  -6.35,   -9.38 ,  30.19,   27.01,   24   ,   20.92],
            [-4.86,  -6.42,   -9.43 ,  30.12,   26.97,   23.89,   20.78],
            [-3.28,  -6.35,   -9.35 ,  30.06,   27.04,   22.34,   20.87],
            [-3.34,  -6.34,   -9.38 ,  29.88,   27.01,   23.92,   20.84],
            [-3.3 ,  -6.34,   -9.4  ,  29.94,   25.35,   23.75,   20.81],
            [-3.28,  -6.36,   -9.45 ,  29.96,   26.91,   23.83,   20.73],
            [-3.26,  -6.34,   -9.39 ,  29.91,   26.8 ,   23.85,   20.8 ],
            [-3.31,  -6.38,   -9.42 ,  29.9 ,   26.84,   23.82,   20.73],
            [-3.29,  -6.41,   -9.37 ,  29.95,   26.83,   23.76,   20.77],
            [-3.27,  -6.36,   -9.42 ,  30   ,   26.87,   23.8 ,   20.72],
            [-2.33,  -5.37,   -9.43 ,  31   ,   27.77,   24.77,   21.69],
            [-3.28,  -6.41,   -9.38 ,  30.03,   26.8 ,   23.65,   20.68],
            [-3.29,  -6.34,   -9.38 ,  30.13,   26.81,   22.7 ,   20.73],
            [-3.28,  -6.38,   -9.42 ,  30.17,   26.87,   23.71,   20.67],
            [-3.32,  -6.35,   -9.41 ,  30.14,   26.84,   22.64,   20.7 ],
            [-3.28,  -6.4 ,   -10.4 ,  30.12,   26.84,   23.72,   20.6 ],
            [-3.38,  -6.46,   -9.57 ,  29.99,   26.71,   23.64,   20.59],
            [-3.33,  -6.36,   -9.43 ,  29.92,   26.8 ,   23.67,   20.61],
            [-3.28,  -6.44,   -9.45 ,  29.73,   26.75,   23.52,   20.57],
            [-3.24,  -6.36,   -9.52 ,  29.54,   26.75,   23.57,   20.46],
            [-3.21,  -6.38,   -9.42 ,  29.57,   26.72,   23.51,   20.45],
            [-3.22,  -6.38,   -9.45 ,  29.51,   26.66,   23.41,   20.39],
            [-3.21,  -6.39,   -9.46 ,  29.56,   26.55,   23.41,   20.39],
            [-3.19,  -6.38,   -9.41 ,  29.54,   26.58,   23.42,   20.32],
            [-3.18,  -6.36,   -9.42 ,  29.63,   26.53,   23.41,   20.34],
            [-3.13,  -6.4 ,   -9.44 ,  29.49,   26.61,   23.32,   20.26],
            [-3.1 ,  -6.32,   -9.44 ,  29.46,   26.61,   23.34,   20.22],
            [-3.08,  -7.01,   -10.07,  29.39,   26.52,   23.33,   20.26],
            [-3.14,  -6.23,   -9.32 ,  29.28,   26.55,   23.26,   19.57],
            [-3.07,  -6.94,   -9.24 ,  29.21,   25.85,   23.31,   20.32],
            [-3.08,  -6.83,   -9.2  ,  29.09,   26.55,   23.33,   20.26],
            [-3.03,  -6.18,   -9.86 ,  28.96,   26.42,   23.34,   20.26],
            [-2.48,  -5.54,   -8.62 ,  29.56,   26.96,   23.84,   20.8 ],
            [-3.03,  -6.14,   -9.25 ,  28.77,   26.36,   23.2 ,   20.11],
            [-3.06,  -6.19,   -9.23 ,  28.82,   26.32,   23.14,   20.09],
            [-3.09,  -6.16,   -9.2  ,  28.71,   26.23,   23.03,   20.1 ],
            [-3.62,  -6.29,   -9.25 ,  28.71,   25.6 ,   23.07,   20.03],
            [-3.09,  -6.22,   -9.3  ,  28.66,   26.1 ,   22.97,   19.93],
            [-3.12,  -6.22,   -9.24 ,  28.76,   26.09,   22.99,   19.95],
            [-3.06,  -6.18,   -9.26 ,  28.75,   26.16,   22.92,   19.93],
            [-3.05,  -6.19,   -9.24 ,  28.13,   26.27,   23.03,   19.44],
            [-3.11,  -6.24,   -9.3  ,  28.57,   26.39,   23.04,   19.96],
            [-3.11,  -6.26,   -9.36 ,  27.88,   26.31,   22.57,   20   ],
            [-3.12,  -6.29,   -9.73 ,  28.07,   26.18,   23.06,   19.89],
            [-3.22,  -6.35,   -9.46 ,  27.76,   25.85,   22.5 ,   19.83],
            [-3.13,  -6.31,   -9.37 ,  27.56,   25.18,   22.43,   19.72],
            [-3.14,  -6.31,   -9.4  ,  27.47,   25.05,   22.49,   19.47],
            [-3.43,  -6.32,   -9.34 ,  27.59,   25.33,   22.46,   19.31],
            [-3.06,  -6.57,   -9.4  ,  27.79,   25.44,   22.39,   19.07],
            [-2.97,  -6.3 ,   -9.65 ,  27.99,   25.61,   22.52,   19.15],
            [-2.98,  -6.34,   -9.35 ,  28.07,   25.86,   22.71,   19.64],
            [-3.06,  -6.58,   -9.57 ,  27.68,   25.87,   23.07,   19.95],
            [-2.8 ,  -6.35,   -9.45 ,  27.22,   25.5 ,   23.32,   20.07],
            [-2.8 ,  -6.41,   -9.5  ,  27   ,   24.82,   22.95,   19.98],
            [-2.9 ,  -6.47,   -9.44 ,  26.57,   24.47,   22.74,   19.53],
            [-2.58,  -6.43,   -9.39 ,  26.25,   23.91,   22.03,   19.21],
            [-2.7 ,  -6.23,   -9.43 ,  25.93,   23.68,   21.49,   18.58],
            [-2.4 ,  -5.97,   -9.25 ,  26.05,   23.63,   21.1 ,   18.22],
            [-2.37,  -5.93,   -9.1  ,  26.3 ,   23.77,   20.94,   18   ],
            [-2.41,  -5.8 ,   -9.01 ,  26.65,   24.01,   21.11,   17.95],
            [-2.39,  -5.67,   -9.02 ,  26.88,   24.26,   21.37,   18.36],
            [-2.21,  -5.45,   -8.71 ,  27.02,   24.53,   21.66,   18.69],
            [-2.08,  -5.21,   -8.44 ,  26.71,   24.36,   21.54,   18.62],
            [-2.04,  -5.14,   -8.26 ,  26.22,   24.02,   21.04,   18.15],
            [-2.14,  -5.11,   -8.46 ,  25.44,   23.29,   20.26,   17.39],
            [-2   ,  -5.09,   -8.2  ,  25.04,   23.01,   19.53,   16.79],
            [-1.82,  -4.75,   -7.94 ,  24.93,   22.76,   19.34,   16.25],
            [-1.98,  -4.87,   -8.12 ,  24.71,   22.44,   19.05,   16.05],
            [-1.91,  -4.74,   -7.64 ,  25.17,   22.95,   19.4 ,   16.33],
            [-1.79,  -4.63,   -7.85 ,  25.22,   23.04,   19.38,   16.33],
            [-1.75,  -4.55,   -7.73 ,  25.08,   23.38,   19.81,   16.6 ],
            [-1.36,  -4.15,   -7.29 ,  25.8 ,   23.69,   20.17,   16.94],
            [-1.92,  -4.34,   -7.52 ,  25.23,   23.45,   19.44,   16.64],
            [-1.51,  -4.36,   -7.8  ,  24.65,   23.1 ,   19.57,   15.95],
            [-1.52,  -4.29,   -7.89 ,  24.03,   22.67,   18.87,   16.04],
            [-1.43,  -4.12,   -7.33 ,  23.62,   22.38,   18.61,   15.75],
            [-1.73,  -4.16,   -7.26 ,  23.4 ,   22.21,   18.83,   15.54],
            [-1.32,  -4.04,   -7.27 ,  23.4 ,   22.16,   18.72,   15.43],
            [-1.24,  -3.97,   -7.17 ,  23.42,   22.09,   18.8 ,   15.55],
            [-1.27,  -3.89,   -7.11 ,  23.78,   22.48,   19.08,   15.76],
            [-1.22,  -3.86,   -7.06 ,  23.93,   22.75,   19.35,   16.09],
            [-1.11,  -3.77,   -7.02 ,  23.91,   22.89,   19.63,   16.31],
            [-1.14,  -3.75,   -6.93 ,  23.57,   22.82,   19.74,   16.43],
            [-0.9 ,  -3.3 ,   -6.24 ,  23.62,   22.76,   19.97,   16.8 ],
            [-0.86,  -3.17,   -6.16 ,  23.26,   22.49,   19.76,   16.6 ],
            [-0.76,  -3.09,   -6.02 ,  23.14,   22.22,   19.61,   16.46],
            [-2.81,  -3.03,   -5.8  ,  22.99,   22.23,   19.54,   16.35],
            [-0.64,  -2.93,   -5.79 ,  23.05,   22.24,   19.53,   16.43],
            [-0.53,  -2.74,   -5.7  ,  23.15,   22.39,   19.71,   16.54],
            [-0.58,  -2.65,   -5.59 ,  23.34,   22.51,   19.93,   16.74],
            [-0.45,  -2.53,   -5.48 ,  23.4 ,   21.94,   19.99,   16.94],
            [-0.43,  -2.49,   -5.45 ,  23.24,   22.74,   20.26,   17.03],
            [-0.28,  -2.34,   -5.24 ,  23.33,   22.63,   20.3 ,   17.13],
            [-0.35,  -2.23,   -5.16 ,  23.05,   22.53,   20.13,   16.22],
            [-0.62,  -2.8 ,   -5.91 ,  22.54,   22.19,   19.76,   16.38],
            [-0.43,  -2.48,   -5.63 ,  22.21,   21.97,   19.6 ,   16.16],
            [-0.42,  -2.39,   -5.42 ,  22.08,   21.81,   19.42,   16.08],
            [-0.35,  -2.3 ,   -5.27 ,  20.9 ,   20.71,   19.23,   16.12],
            [-0.35,  -2.3 ,   -6.27 ,  21.82,   21.59,   19.5 ,   16.21],
            [-0.41,  -2.38,   -5.48 ,  21.6 ,   21.62,   19.62,   16.48],
            [-0.27,  -2.06,   -5.06 ,  21.99,   21.88,   20.06,   15.85],
            [-0.14,  -1.99,   -4.95 ,  22.1 ,   22.11,   20.36,   17.29],
            [-0.08,  -1.86,   -4.98 ,  21.74,   21.77,   20.14,   17.14],
            [0.06 ,  -1.69,   -4.6  ,  21.54,   21.47,   19.8 ,   16.84],
            [0.11 ,  -1.62,   -4.74 ,  21.41,   21.67,   19.94,   16.94],
            [-0.03,  -1.74,   -4.79 ,  21.07,   21.39,   19.89,   16.85],
            [-0.01,  -1.74,   -4.77 ,  20.52,   20.98,   19.54,   16.48],
            [0.07 ,  -1.72,   -4.8  ,  19.95,   18.84,   18.84,   15.81],
            [-0.02,  -1.94,   -5.2  ,  19.55,   19.97,   18.39,   15.35],
            [-0.03,  -2.01,   -5.32 ,  20.06,   20.51,   18.8 ,   15.69],
            [-0.02,  -2   ,   -5.41 ,  20.7 ,   21.2 ,   19.58,   16.54],
            [-1.16,  -1.97,   -5.4  ,  20.48,   21.08,   19.63,   16.65],
            [-0.02,  -2.05,   -5.53 ,  19.53,   20.24,   18.55,   15.61],
            [0.06 ,  -1.98,   -5.53 ,  19.29,   19.89,   18.07,   14.91],
            [0.13 ,  -2   ,   -5.62 ,  19.59,   20.19,   18.29,   15.2 ],
            [0.1  ,  -2.09,   -6.67 ,  20.09,   20.72,   19   ,   15.88],
            [0.08 ,  -2.18,   -5.77 ,  20.07,   20.81,   19.16,   16.05],
            [0    ,  -2.3 ,   -6.08 ,  19.42,   20.14,   16.68,   15.37],
            [0.16 ,  -2.72,   -5.46 ,  19.35,   19.68,   17.63,   13.5 ],
            [0.22 ,  -2.01,   -5.48 ,  19.38,   19.73,   17.46,   14.21],
            [0.21 ,  -4.01,   -5.71 ,  19.65,   19.97,   17.73,   14.44],
            [0.11 ,  -2.23,   -5.85 ,  19.72,   20.05,   17.93,   14.57],
            [0.22 ,  -2.26,   -5.96 ,  19.88,   20.33,   17.98,   14.67],
            [0.16 ,  -2.4 ,   -6.03 ,  19.76,   20.1 ,   17.75,   14.34],
            [0.19 ,  -2.33,   -6.09 ,  19.36,   19.78,   16.6 ,   13.83],
            [-0.01,  -2.49,   -6.78 ,  19.03,   19.31,   16.71,   13.26],
            [0.03 ,  -2.66,   -6.33 ,  19.13,   19.28,   16.51,   13   ],
            [-0.44,  -2.69,   -6.36 ,  19.63,   19.58,   16.79,   12.71],
            [0.03 ,  -2.65,   -6.38 ,  19.89,   19.77,   16.98,   13.34],
            [0.27 ,  -2.32,   -6.03 ,  19.94,   19.38,   16.88,   12.83],
            [-0.14,  -2.96,   -6.67 ,  19.03,   18.86,   15.58,   12.27],
            [-0.48,  -3.93,   -8.06 ,  17.34,   17.91,   15.3 ,   11.71],
            [-0.74,  -4.13,   -8.34 ,  17.42,   18.18,   15.62,   12.01],
            [-0.65,  -4.18,   -8.42 ,  18.24,   18.57,   15.9 ,   12.39],
            [-0.58,  -4.06,   -8.32 ,  17.6 ,   18.23,   15.58,   11.9 ],
            [-0.91,  -4.32,   -8.46 ,  17.26,   17.51,   14.82,   11.07],
            [-0.88,  -4.14,   -8.15 ,  17.49,   17.66,   14.81,   11.24],
            [-0.74,  -4.13,   -8.29 ,  17.98,   18.09,   15.38,   11.64],
            [-0.82,  -4.4 ,   -8.47 ,  18.34,   18.53,   15.8 ,   12.05],
            [-0.97,  -4.53,   -8.87 ,  18.16,   18.39,   15.6 ,   11.86],
            [-0.92,  -4.8 ,   -9.19 ,  17.82,   17.97,   14.92,   11.35]]

        self.arrFirmware = [
            [-6 ,-12,-19,59, 53, 47, 41],
            [-6 ,-13,-19,60, 54, 48, 42],
            [-6 ,-13,-19,60, 53, 48, 42],
            [-6 ,-13,-21,60, 54, 47, 42],
            [-6 ,-13,-18,60, 54, 48, 42],
            [-6 ,-13,-21,60, 54, 48, 42],
            [-7 ,-13,-19,60, 54, 48, 42],
            [-7 ,-13,-19,60, 54, 48, 42],
            [-7 ,-13,-19,60, 54, 48, 42],
            [-6 ,-13,-19,60, 54, 45, 39],
            [-7 ,-13,-22,60, 54, 48, 42],
            [-7 ,-13,-19,60, 54, 48, 42],
            [-6 ,-13,-19,60, 54, 48, 39],
            [-7 ,-13,-19,60, 54, 48, 42],
            [-7 ,-13,-19,61, 54, 48, 42],
            [-7 ,-13,-19,61, 54, 48, 42],
            [-7 ,-13,-19,61, 54, 48, 42],
            [-7 ,-13,-19,61, 54, 48, 42],
            [-7 ,-13,-19,61, 52, 48, 42],
            [-7 ,-13,-19,61, 54, 48, 42],
            [-7 ,-13,-19,60, 54, 48, 42],
            [-10,-13,-19,60, 54, 48, 42],
            [-7 ,-13,-19,60, 54, 45, 42],
            [-7 ,-13,-19,60, 54, 48, 42],
            [-7 ,-13,-19,60, 51, 48, 42],
            [-7 ,-13,-19,60, 54, 48, 41],
            [-7 ,-13,-19,60, 54, 48, 42],
            [-7 ,-13,-19,60, 54, 48, 41],
            [-7 ,-13,-19,60, 54, 48, 42],
            [-7 ,-13,-19,60, 54, 48, 41],
            [-5 ,-11,-19,62, 56, 50, 43],
            [-7 ,-13,-19,60, 54, 47, 41],
            [-7 ,-13,-19,60, 54, 45, 41],
            [-7 ,-13,-19,60, 54, 47, 41],
            [-7 ,-13,-19,60, 54, 45, 41],
            [-7 ,-13,-21,60, 54, 47, 41],
            [-7 ,-13,-19,60, 53, 47, 41],
            [-7 ,-13,-19,60, 54, 47, 41],
            [-7 ,-13,-19,59, 54, 47, 41],
            [-6 ,-13,-19,59, 54, 47, 41],
            [-6 ,-13,-19,59, 53, 47, 41],
            [-6 ,-13,-19,59, 53, 47, 41],
            [-6 ,-13,-19,59, 53, 47, 41],
            [-6 ,-13,-19,59, 53, 47, 41],
            [-6 ,-13,-19,59, 53, 47, 41],
            [-6 ,-13,-19,59, 53, 47, 41],
            [-6 ,-13,-19,59, 53, 47, 40],
            [-6 ,-14,-20,59, 53, 47, 41],
            [-6 ,-12,-19,59, 53, 47, 39],
            [-6 ,-14,-18,58, 52, 47, 41],
            [-6 ,-14,-18,58, 53, 47, 41],
            [-6 ,-12,-20,58, 53, 47, 41],
            [-5 ,-11,-17,59, 54, 48, 42],
            [-6 ,-12,-19,58, 53, 46, 40],
            [-6 ,-12,-18,58, 53, 46, 40],
            [-6 ,-12,-18,57, 52, 46, 40],
            [-7 ,-13,-19,57, 51, 46, 40],
            [-6 ,-12,-19,57, 52, 46, 40],
            [-6 ,-12,-18,58, 52, 46, 40],
            [-6 ,-12,-19,58, 52, 46, 40],
            [-6 ,-12,-18,56, 53, 46, 39],
            [-6 ,-12,-19,57, 53, 46, 40],
            [-6 ,-13,-19,56, 53, 45, 40],
            [-6 ,-13,-19,56, 52, 46, 40],
            [-6 ,-13,-19,56, 52, 45, 40],
            [-6 ,-13,-19,55, 50, 45, 39],
            [-6 ,-13,-19,55, 50, 45, 39],
            [-7 ,-13,-19,55, 51, 45, 39],
            [-6 ,-13,-19,56, 51, 45, 38],
            [-6 ,-13,-19,56, 51, 45, 38],
            [-6 ,-13,-19,56, 52, 45, 39],
            [-6 ,-13,-19,55, 52, 46, 40],
            [-6 ,-13,-19,54, 51, 47, 40],
            [-6 ,-13,-19,54, 50, 46, 40],
            [-6 ,-13,-19,53, 49, 45, 39],
            [-5 ,-13,-19,53, 48, 44, 38],
            [-5 ,-12,-19,52, 47, 43, 37],
            [-5 ,-12,-19,52, 47, 42, 36],
            [-5 ,-12,-18,53, 48, 42, 36],
            [-5 ,-12,-18,53, 48, 42, 36],
            [-5 ,-11,-18,54, 49, 43, 37],
            [-4 ,-11,-17,54, 49, 43, 37],
            [-4 ,-10,-17,53, 49, 43, 37],
            [-4 ,-10,-17,52, 48, 42, 36],
            [-4 ,-10,-17,51, 47, 41, 35],
            [-4 ,-10,-16,50, 46, 39, 34],
            [-4 ,-10,-16,50, 46, 39, 33],
            [-4 ,-10,-16,49, 45, 38, 32],
            [-4 ,-9 ,-15,50, 46, 39, 33],
            [-4 ,-9 ,-16,50, 46, 39, 33],
            [-4 ,-9 ,-15,50, 47, 40, 33],
            [-3 ,-8 ,-15,52, 47, 40, 34],
            [-4 ,-9 ,-15,50, 47, 39, 33],
            [-3 ,-9 ,-16,49, 46, 39, 32],
            [-3 ,-9 ,-16,48, 45, 38, 32],
            [-3 ,-8 ,-15,47, 45, 37, 32],
            [-3 ,-8 ,-15,47, 44, 38, 31],
            [-3 ,-8 ,-15,47, 44, 37, 31],
            [-2 ,-8 ,-14,47, 44, 38, 31],
            [-3 ,-8 ,-14,48, 45, 38, 32],
            [-2 ,-8 ,-14,48, 46, 39, 32],
            [-2 ,-8 ,-14,48, 46, 39, 33],
            [-2 ,-8 ,-14,47, 46, 39, 33],
            [-2 ,-7 ,-12,47, 46, 40, 34],
            [-2 ,-6 ,-12,47, 45, 40, 33],
            [-2 ,-6 ,-12,46, 44, 39, 33],
            [-6 ,-6 ,-12,46, 44, 39, 33],
            [-1 ,-6 ,-12,46, 44, 39, 33],
            [-1 ,-5 ,-11,46, 45, 39, 33],
            [-1 ,-5 ,-11,47, 45, 40, 33],
            [-1 ,-5 ,-11,47, 44, 40, 34],
            [-1 ,-5 ,-11,46, 45, 41, 34],
            [-1 ,-5 ,-10,47, 45, 41, 34],
            [-1 ,-4 ,-10,46, 45, 40, 32],
            [-1 ,-6 ,-12,45, 44, 40, 33],
            [-1 ,-5 ,-11,44, 44, 39, 32],
            [-1 ,-5 ,-11,44, 44, 39, 32],
            [-1 ,-5 ,-11,42, 41, 38, 32],
            [-1 ,-5 ,-13,44, 43, 39, 32],
            [-1 ,-5 ,-11,43, 43, 39, 33],
            [-1 ,-4 ,-10,44, 44, 40, 32],
            [0  ,-4 ,-10,44, 44, 41, 35],
            [0  ,-4 ,-10,43, 44, 40, 34],
            [0  ,-3 ,-9 ,43, 43, 40, 34],
            [0  ,-3 ,-9 ,43, 43, 40, 34],
            [0  ,-3 ,-10,42, 43, 40, 34],
            [0  ,-3 ,-10,41, 42, 39, 33],
            [0  ,-3 ,-10,40, 38, 38, 32],
            [0  ,-4 ,-10,39, 40, 37, 31],
            [0  ,-4 ,-11,40, 41, 38, 31],
            [0  ,-4 ,-11,41, 42, 39, 33],
            [-2 ,-4 ,-11,41, 42, 39, 33],
            [0  ,-4 ,-11,39, 40, 37, 31],
            [0  ,-4 ,-11,39, 40, 36, 30],
            [0  ,-4 ,-11,39, 40, 37, 30],
            [0  ,-4 ,-13,40, 41, 38, 32],
            [0  ,-4 ,-12,40, 42, 38, 32],
            [0  ,-5 ,-12,39, 40, 33, 31],
            [0  ,-5 ,-11,39, 39, 35, 27],
            [0  ,-4 ,-11,39, 39, 35, 28],
            [0  ,-8 ,-11,39, 40, 35, 29],
            [0  ,-4 ,-12,39, 40, 36, 29],
            [0  ,-5 ,-12,40, 41, 36, 29],
            [0  ,-5 ,-12,40, 40, 36, 29],
            [0  ,-5 ,-12,39, 40, 33, 28],
            [0  ,-5 ,-14,38, 39, 33, 27],
            [0  ,-5 ,-13,38, 39, 33, 26],
            [-1 ,-5 ,-13,39, 39, 34, 25],
            [0  ,-5 ,-13,40, 40, 34, 27],
            [1  ,-5 ,-12,40, 39, 34, 26],
            [0  ,-6 ,-13,38, 38, 31, 25],
            [-1 ,-8 ,-16,35, 36, 31, 23],
            [-1 ,-8 ,-17,35, 36, 31, 24],
            [-1 ,-8 ,-17,36, 37, 32, 25],
            [-1 ,-8 ,-17,35, 36, 31, 24],
            [-2 ,-9 ,-17,35, 35, 30, 22],
            [-2 ,-8 ,-16,35, 35, 30, 22],
            [-1 ,-8 ,-17,36, 36, 31, 23],
            [-2 ,-9 ,-17,37, 37, 32, 24],
            [-2 ,-9 ,-18,36, 37, 31, 24],
            [-2 ,-10,-18,36, 36, 30, 23]]

    def GetCalSize(self):
        """Return the number of calibraton data if any, otherwise -1 

        Returns:
            Integer the number of calibraton data if any, otherwise -1  
		"""
        if (self.m_arrSignalGeneratorEmbeddedCalibrationActual30DBM):
            return len(self.m_arrSignalGeneratorEmbeddedCalibrationActual30DBM)
        else:
            return -1

    def DeleteCal(self):
        """Delete calibration data collection 
		"""
        self.m_arrSignalGeneratorEmbeddedCalibrationActual30DBM = None

    def InitializeCal(self, nSize, sLine, sReport):
        """Initialize calibration data collection 
        
        Parameters:   
            nSize   -- Size of the collection
            sLine   -- Line of text to process and create the collection
            sReport -- Embedded calibration Signal Generator data text
        Returns:
            String Embedded calibration Signal Generator data received
		"""
        sReport = ""

        self.m_arrSignalGeneratorEmbeddedCalibrationActual30DBM = [-30.0] * nSize

        if (not sLine):
            return sReport

        if nSize < 164:
            return sReport
            
        # skip leading '$q'
        nSize -=2 

        #Values using 10*delta from the value delivered when compared with 30dBm.
        #For instance if value delivered for a frequency is -28.5dBm, that is a +1.5dB difference
        #therefore a 1.5*10=15 value. If the value delivered is -33.2 that is a -3.2dB difference
        #therefore a -32 value.

        self.m_arrSignalGeneratorEmbeddedCalibrationActual30DBM =\
                    [ (-30.0 + float( c_int8( ord(c) ).value ) / 10.0) for c in sLine[2:] ]
            
        for nInd in range(nSize):
            if nInd and ((nInd % 16) == 0):
                sReport += '\n'
            sReport += '{:04.1f}'.format(self.m_arrSignalGeneratorEmbeddedCalibrationActual30DBM[nInd]) 
            if (nInd < nSize - 1):
                sReport += ","

        return sReport

    def GetEstimatedAmplitudeArray(self, dFrequencyMHZ):
        """Return estimated output power level array with 8 different power position for specific frequency

        Parameters:
            dFrequencyMHZ -- Frequency of interest 
        Returns:
		    List Amplitude array
		"""
        arrReturn = []

        if (self.m_arrSignalGeneratorEmbeddedCalibrationActual30DBM):
            nFreqInd = self.GetClosestFrequencyIndex(dFrequencyMHZ)
            if (nFreqInd >= 0):
                arrReturn = [0.0]*8
                dValue30DBM = self.m_arrSignalGeneratorEmbeddedCalibrationActual30DBM[nFreqInd]

                arrReturn[0] = dValue30DBM + self.m_arrDeltaAmplitude[nFreqInd][2]
                arrReturn[1] = dValue30DBM + self.m_arrDeltaAmplitude[nFreqInd][1]
                arrReturn[2] = dValue30DBM + self.m_arrDeltaAmplitude[nFreqInd][0]
                arrReturn[3] = dValue30DBM

                arrReturn[4] = dValue30DBM + self.m_arrDeltaAmplitude[nFreqInd][6]
                arrReturn[5] = dValue30DBM + self.m_arrDeltaAmplitude[nFreqInd][5]
                arrReturn[6] = dValue30DBM + self.m_arrDeltaAmplitude[nFreqInd][4]
                arrReturn[7] = dValue30DBM + self.m_arrDeltaAmplitude[nFreqInd][3]

        return arrReturn

    def GetClosestFrequencyIndex(self, dFrequencyMHZ):
        """Return the index of the calibration data collection based on specific frequency 

        Parameters:
            dFrequencyMHZ -- Frequency of interest 
        Returns:
		    Integer the closet frequency Index
		"""
        nFreqInd = 0
        if (self.m_arrSignalGeneratorEmbeddedCalibrationActual30DBM):
            #search by brute force, if this is considered too slow, can be replace by binary search or something else such a hash
            for nInd in range(len(self.m_arrSignalGeneratorCalRanges_KHZ), 0, -1):
                dStartFreqMHZ = self.m_arrSignalGeneratorCalRanges_KHZ[nInd] / 1000.0
                if (dStartFreqMHZ <= dFrequencyMHZ):
                    nFreqInd = nInd
                    break

        return nFreqInd

    def GetEstimatedAmplitude(self, dFrequencyMHZ, bHighPowerSwitch, nPowerLevel):
        """Returns best matching amplitude value based on internal -30dBm calibration table, and configured power switch/attenuator
        If not available, this returns the estimated value based on hardcoded measured amplitude values

        Parameters:
            dFrequencyMHZ    -- Frequency of interest
            bHighPowerSwitch -- True if it is disable, otherwise False
            nPowerLevel      -- Power level from min. 4 to max. 0
        Returns:
		    Float Estimated amplitude in dBm
		"""
        dValueDBM = 0
        dValue30DBM = -30
        nFreqInd = self.GetClosestFrequencyIndex(dFrequencyMHZ)

        if (self.m_arrSignalGeneratorEmbeddedCalibrationActual30DBM):
            dValue30DBM = self.m_arrSignalGeneratorEmbeddedCalibrationActual30DBM[nFreqInd]

        if (bHighPowerSwitch):
            if(nPowerLevel == 3):
                dValueDBM = dValue30DBM + self.m_arrDeltaAmplitude[nFreqInd][3]
            elif(nPowerLevel == 2):
                dValueDBM = dValue30DBM + self.m_arrDeltaAmplitude[nFreqInd][4]
            elif(nPowerLevel == 1):
                dValueDBM = dValue30DBM + self.m_arrDeltaAmplitude[nFreqInd][5]
            elif(nPowerLevel == 0): 
                dValueDBM = dValue30DBM + self.m_arrDeltaAmplitude[nFreqInd][6]
        else:
            if(nPowerLevel == 3): 
                dValueDBM = dValue30DBM   #dValue30DBM is correct already
            elif(nPowerLevel == 2): 
                dValueDBM = dValue30DBM + self.m_arrDeltaAmplitude[nFreqInd][0]
            elif(nPowerLevel == 1): 
                dValueDBM = dValue30DBM + self.m_arrDeltaAmplitude[nFreqInd][1]
            elif(nPowerLevel == 0): 
                dValueDBM = dValue30DBM + self.m_arrDeltaAmplitude[nFreqInd][2]

        return dValueDBM
