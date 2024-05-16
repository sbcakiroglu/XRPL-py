from xrpl.clients import JsonRpcClient
from xrpl.wallet import generate_faucet_wallet
from xrpl.core import addresscodec

# XRPL ağı için JSON-RPC URL'si
JSON_RPC_URL = "https://s.altnet.rippletest.net:51234/"

# JSON-RPC istemcisini oluşturun
client = JsonRpcClient(JSON_RPC_URL)

# Testnet musluğunu kullanarak cüzdan oluşturma:
# https://xrpl.org/xrp-testnet-faucet.html
test_wallet = generate_faucet_wallet(client, debug=True)

# X-adresini türetme işlemi
test_account = test_wallet.classic_address
test_xaddress = addresscodec.classic_address_to_xaddress(test_account, tag=12345, is_test_network=True)

# Klasik adresi ve X-adresini yazdırma
print("\nClassic address:\n\n", test_account)
print("X-address:\n\n", test_xaddress)
