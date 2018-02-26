#!/usr/bin/env bash
#@ c0demech || 2018
## THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
## IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
## FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
## AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
## LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
## OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
## SOFTWARE.
#@@@@@@@@@@@@@@@@@@@@@@@@@@
## Mining ETH || Tested with XFX RX570 Cards 
#@ amdgpu-pro-17.40-483984
#@ https://github.com/OhGodACompany/OhGodATool
#@ Make sure to stop mining before running this script
#@  
#@

ohgodatool="~/repo/OhGodATool/ohgodatool"
# Be careful if you decide to change these
mclock=2000 #default was ~
cclock=1100 #default was 1250

for card in {0..6}; do
  if [[ -e /sys/class/drm/card$i/device/pp_table ]]; then
     echo "Card Detected in Slot: $i"
     echo "Updating memory clock to: $mclock"
     echo "Updating core   clock to: $cclock"
     $ohgodatool -i $card --mem-state -1 --mem-clock $mclock
     $ohgodatool -i $card --core-state -1 --core-clock $cclock
  fi
done
