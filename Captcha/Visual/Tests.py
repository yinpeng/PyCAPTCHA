""" Captcha.Visual.Tests

Visual CAPTCHA tests
"""
#
# PyCAPTCHA Package
# Copyright (C) 2004 Micah Dowty <micah@navi.cx>
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
#

from Captcha.Visual import Text, Backgrounds, Distortions, ImageCaptcha, Pictures
from Captcha import Words


class PseudoGimpy(ImageCaptcha):
    def getLayers(self):
        word = Words.defaultWordList.pick()
        self.addSolution(word)
        return [
            Backgrounds.CroppedImage(),
            Text.TextLayer(word, borderSize=1),
            #Distortions.WigglyBlocks(),
            Distortions.SineWarp(),
            #Backgrounds.RandomDots(),
            ]

### The End ###
