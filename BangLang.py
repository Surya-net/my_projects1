import argparse

# BangLang for coding in bengali 
# I know it's very simple and slow. But it was my dream project.
অনুবাদ = {
    # Keywords
    'পদ্ধতি': 'def',
    'ফিরাও': 'return',
    'যদি': 'if',
    'অবশেষে': 'else',
    'অবশেষে_যদি': 'elif',
    'প্রতিটি': 'for',
    'যখন': 'while',
    'মধ্যে': 'in',
    'হিসেবে': 'as',
    'আমদানি': 'import',
    'থেকে': 'from',
    'চেষ্টা': 'try',
    'ব্যতীত': 'except',
    'শেষে': 'finally',
    'সাথে': 'with',
    'ভাঙ': 'break',
    'চালিয়ে_যাও': 'continue',
    'ফাঁকা': 'pass',
    'শ্রেণি': 'class',
    'না': 'not',
    'এবং': 'and',
    'বা': 'or',
    'ছোট': 'lambda',
    'থিম': 'await',
    'ফল': 'yield',
    'গ্লোবাল': 'global',
    'স্থানীয়': 'nonlocal',

    # Built-in defs
    # Please add other functions.
    'লিখ': 'print',
    'দৈর্ঘ্য': 'len',
    'পরিসীমা': 'range',
    'পূর্ণসংখ্যা': 'int',
    'দশমিক': 'float',
    'লেখা': 'str',
    'তালিকা': 'list',
    'কোষ': 'dict',
    'নিন': 'input',
    'খুলো': 'open',
    'ধরণ': 'type',
    'ধরন_কি': 'isinstance'
}

def চালাও(কোড):
    
    for bn, py in অনুবাদ.items():
        কোড = কোড.replace(bn, py)
    exec(কোড)

def main():
    parser = argparse.ArgumentParser(description="BangLang: Bengali Python Interpreter")
    parser.add_argument('--code', type=str, help='Path to your .bang file')
    args = parser.parse_args()

    if args.code:
        with open(args.code, 'r', encoding='utf-8') as f:
            code = f.read()
        চালাও(code)
    else:
        print("কোডের ফাইলটি এন্টার করুন: banglang --code hello.bang")

if __name__ == "__main__":
  # Fully Made by Surya (yeah me bro!)
    main()
