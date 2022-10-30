main_str = """
"""
str_diсt_ = {}
def get_count_char(str_) :
     str_ = "".join(str_.lower().split())
     for words_ in str_:
         if words_.isalpha() and words_ not in str_diсt_:
             str_diсt_[words_] = 1
         else:
             if words_.isalpha() and words_ in str_diсt_:
                 str_diсt_[words_] += 1
     return str_diсt_

def new_diсt_(str_diсt_):
    sum_ = sum(str_diсt_.values())
    for i in str_diсt_:
        str_diсt_[i] = round((str_diсt_[i]/sum_) * 100, 3)
    print(sum(str_diсt_.values()))
    return str_diсt_

print(get_count_char(main_str))