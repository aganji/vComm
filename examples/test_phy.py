# Adding vlc phy to system path
import sys
sys.path.append('..')

# import vlc phy
import tx_phy

# create phy objct
phyObj = tx_phy.vlc_tx()
# Send test data
phyObj.send_data('1101001')
phyObj.cleanuo()