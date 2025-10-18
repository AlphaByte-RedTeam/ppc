# simulasi transfer uang dengan bank
# sistem perbankan:
# 1. bisa cek nomor rekening
# 2. bisa cek saldo
# 3. bisa transfer uang ke rekening terdaftar
# 4. tidak bisa transfer uang ke rekening tidak terdaftar
# 5. tidak bisa transfer uang jika saldo tidak mencukupi
# menggunakan functional programming


# currency: USD
account_db = {
    # account_num: balance
    "0930079405": {"balance": 100, "name": "Andrew"},  # Pentransfer
    "123456789": {"balance": 500, "name": "James"},  # Penerima
}


def check_balance(account: str):
    if account in account_db:
        print(f"Name: {account_db[account]['name']}")
        print(f"Balance: {account_db[account]['balance']}")
        return account_db[account]["balance"]  # return balance nya
    else:
        print(f"Account '{account}' not found")


def transfer(sender_account: str, dest_account: str, transfer_amount):
    sender_balance = account_db[sender_account]["balance"]
    if dest_account not in account_db:
        print(f"Account '{dest_account}' not found")
    elif sender_balance < transfer_amount:
        print("Insufficient balance")
    else:
        account_db[sender_account]["balance"] -= transfer_amount
        account_db[dest_account]["balance"] += transfer_amount
        print(
            f"Transfer to {account_db[dest_account]['name']} with amount USD {transfer_amount} successful"
        )


def main():
    sender_acc = "0930079405"  # Andrew
    dest_acc = "123456789"  # James
    tf_amt = 150
    balance = check_balance("0930079405")
    print(f"Current balance: {balance}")
    print("")
    transfer(sender_account=sender_acc, dest_account=dest_acc, transfer_amount=tf_amt)
    print("")
    balance = check_balance("123456789")
    print(f"Current balance: {balance}")


if __name__ == "__main__":
    main()
