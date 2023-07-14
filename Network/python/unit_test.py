from model import *

seed = DeMes.generateSeedByPhrases(['hello', 'my', 'dear'])
account = DeMes.newAccount()
account['private_key'] = DeMes.generatePrivateKeyBySeed(seed)
account['public_key'] = account['private_key'].get_public_key()
#print(account)

sign = DeMes.sign(input('text to sign>>'), account['private_key'])
print(sign)

text = input('Enter the same text to verify>>')
sign = input('Signature>>')

print("Verified" if DeMes.verify(text, sign, account['public_key']) else 'Unverified')