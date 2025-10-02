import argparse, sys
"""BangLang
********

This is a program, by Surya. by using this program you can run python programs in bengali.

Repository: https://github.com/Surya-net/my_prjects/
Devoloper: Suryalal Singha GitHub: www.github.com/Surya-net Email: surya.geek.email@gmail.com"""

# BangLang for coding in bengali 
# I know it's very simple and slow. But it was my dream project.
dictionary = {
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

def run(code):
    
    for bn, py in dictionary.items():
        code = code.replace(bn, py)
    exec(code)

def main():
    parser = argparse.ArgumentParser(description="BangLang: Bengali Python Interpreter")
    parser.add_argument('--code', type=str, help='Path to your .bang file')
    args = parser.parse_args()

    if args.code:
        if not ".bang" in args.code:
            print("দয়া করে '.bang' এক্সটেনশনটি ব্যবহার করে আবার চেষ্টা করুন।")
            sys.exit(1)
        with open(args.code, 'r', encoding='utf-8') as f:
            code = f.read()
        run(code)
    else:
        print("কোডের ফাইলটি এভাবে এন্টার করুন: banglang --code hello.bang")

if __name__ == "__main__":
    # Fully Made by Surya (yeah me bro!)
    # If you're bengali please contribute to my project.
    main()
    # This is a experimental project so please don't judge.
