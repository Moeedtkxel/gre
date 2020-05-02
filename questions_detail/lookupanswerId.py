# import csv
from datetime import datetime

startTime = datetime.now()

#
# def powerset(s):
#     a = ['']
#     for i, c in enumerate(s):
#         for k in range(2 ** i):
#             a.append(a[k] + c)
#     return a
#
#
# with open('my_file.csv', 'w') as f:
#     [f.write('{0},{1}\n'.format(key, value)) for key, value in dict512.items()]
#
# z = powerset('abcdefghi')
# print(len(z))


#
# powerset = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'ab', 'ac', 'ad', 'ae', 'af', 'ag', 'ah', 'ai', 'bc', 'bd',
#             'be', 'bf', 'bg', 'bh', 'bi', 'cd', 'ce', 'cf', 'cg', 'ch', 'ci', 'de', 'df', 'dg', 'dh', 'di', 'ef', 'eg',
#             'eh', 'ei', 'fg', 'fh', 'fi', 'gh', 'gi', 'hi', 'abc', 'abd', 'abe', 'abf', 'abg', 'abh', 'abi', 'acd',
#             'ace', 'acf', 'acg', 'ach', 'aci', 'ade', 'adf', 'adg', 'adh', 'adi', 'aef', 'aeg', 'aeh', 'aei', 'afg',
#             'afh', 'afi', 'agh', 'agi', 'ahi', 'bcd', 'bce', 'bcf', 'bcg', 'bch', 'bci', 'bde', 'bdf', 'bdg', 'bdh',
#             'bdi', 'bef', 'beg', 'beh', 'bei', 'bfg', 'bfh', 'bfi', 'bgh', 'bgi', 'bhi', 'cde', 'cdf', 'cdg', 'cdh',
#             'cdi', 'cef', 'ceg', 'ceh', 'cei', 'cfg', 'cfh', 'cfi', 'cgh', 'cgi', 'chi', 'def', 'deg', 'deh', 'dei',
#             'dfg', 'dfh', 'dfi', 'dgh', 'dgi', 'dhi', 'efg', 'efh', 'efi', 'egh', 'egi', 'ehi', 'fgh', 'fgi', 'fhi',
#             'ghi', 'abcd', 'abce', 'abcf', 'abcg', 'abch', 'abci', 'abde', 'abdf', 'abdg', 'abdh', 'abdi', 'abef',
#             'abeg', 'abeh', 'abei', 'abfg', 'abfh', 'abfi', 'abgh', 'abgi', 'abhi', 'acde', 'acdf', 'acdg', 'acdh',
#             'acdi', 'acef', 'aceg', 'aceh', 'acei', 'acfg', 'acfh', 'acfi', 'acgh', 'acgi', 'achi', 'adef', 'adeg',
#             'adeh', 'adei', 'adfg', 'adfh', 'adfi', 'adgh', 'adgi', 'adhi', 'aefg', 'aefh', 'aefi', 'aegh', 'aegi',
#             'aehi', 'afgh', 'afgi', 'afhi', 'aghi', 'bcde', 'bcdf', 'bcdg', 'bcdh', 'bcdi', 'bcef', 'bceg', 'bceh',
#             'bcei', 'bcfg', 'bcfh', 'bcfi', 'bcgh', 'bcgi', 'bchi', 'bdef', 'bdeg', 'bdeh', 'bdei', 'bdfg', 'bdfh',
#             'bdfi', 'bdgh', 'bdgi', 'bdhi', 'befg', 'befh', 'befi', 'begh', 'begi', 'behi', 'bfgh', 'bfgi', 'bfhi',
#             'bghi', 'cdef', 'cdeg', 'cdeh', 'cdei', 'cdfg', 'cdfh', 'cdfi', 'cdgh', 'cdgi', 'cdhi', 'cefg', 'cefh',
#             'cefi', 'cegh', 'cegi', 'cehi', 'cfgh', 'cfgi', 'cfhi', 'cghi', 'defg', 'defh', 'defi', 'degh', 'degi',
#             'dehi', 'dfgh', 'dfgi', 'dfhi', 'dghi', 'efgh', 'efgi', 'efhi', 'eghi', 'fghi', 'abcde', 'abcdf', 'abcdg',
#             'abcdh', 'abcdi', 'abcef', 'abceg', 'abceh', 'abcei', 'abcfg', 'abcfh', 'abcfi', 'abcgh', 'abcgi', 'abchi',
#             'abdef', 'abdeg', 'abdeh', 'abdei', 'abdfg', 'abdfh', 'abdfi', 'abdgh', 'abdgi', 'abdhi', 'abefg', 'abefh',
#             'abefi', 'abegh', 'abegi', 'abehi', 'abfgh', 'abfgi', 'abfhi', 'abghi', 'acdef', 'acdeg', 'acdeh', 'acdei',
#             'acdfg', 'acdfh', 'acdfi', 'acdgh', 'acdgi', 'acdhi', 'acefg', 'acefh', 'acefi', 'acegh', 'acegi', 'acehi',
#             'acfgh', 'acfgi', 'acfhi', 'acghi', 'adefg', 'adefh', 'adefi', 'adegh', 'adegi', 'adehi', 'adfgh', 'adfgi',
#             'adfhi', 'adghi', 'aefgh', 'aefgi', 'aefhi', 'aeghi', 'afghi', 'bcdef', 'bcdeg', 'bcdeh', 'bcdei', 'bcdfg',
#             'bcdfh', 'bcdfi', 'bcdgh', 'bcdgi', 'bcdhi', 'bcefg', 'bcefh', 'bcefi', 'bcegh', 'bcegi', 'bcehi', 'bcfgh',
#             'bcfgi', 'bcfhi', 'bcghi', 'bdefg', 'bdefh', 'bdefi', 'bdegh', 'bdegi', 'bdehi', 'bdfgh', 'bdfgi', 'bdfhi',
#             'bdghi', 'befgh', 'befgi', 'befhi', 'beghi', 'bfghi', 'cdefg', 'cdefh', 'cdefi', 'cdegh', 'cdegi', 'cdehi',
#             'cdfgh', 'cdfgi', 'cdfhi', 'cdghi', 'cefgh', 'cefgi', 'cefhi', 'ceghi', 'cfghi', 'defgh', 'defgi', 'defhi',
#             'deghi', 'dfghi', 'efghi', 'abcdef', 'abcdeg', 'abcdeh', 'abcdei', 'abcdfg', 'abcdfh', 'abcdfi', 'abcdgh',
#             'abcdgi', 'abcdhi', 'abcefg', 'abcefh', 'abcefi', 'abcegh', 'abcegi', 'abcehi', 'abcfgh', 'abcfgi',
#             'abcfhi', 'abcghi', 'abdefg', 'abdefh', 'abdefi', 'abdegh', 'abdegi', 'abdehi', 'abdfgh', 'abdfgi',
#             'abdfhi', 'abdghi', 'abefgh', 'abefgi', 'abefhi', 'abeghi', 'abfghi', 'acdefg', 'acdefh', 'acdefi',
#             'acdegh', 'acdegi', 'acdehi', 'acdfgh', 'acdfgi', 'acdfhi', 'acdghi', 'acefgh', 'acefgi', 'acefhi',
#             'aceghi', 'acfghi', 'adefgh', 'adefgi', 'adefhi', 'adeghi', 'adfghi', 'aefghi', 'bcdefg', 'bcdefh',
#             'bcdefi', 'bcdegh', 'bcdegi', 'bcdehi', 'bcdfgh', 'bcdfgi', 'bcdfhi', 'bcdghi', 'bcefgh', 'bcefgi',
#             'bcefhi', 'bceghi', 'bcfghi', 'bdefgh', 'bdefgi', 'bdefhi', 'bdeghi', 'bdfghi', 'befghi', 'cdefgh',
#             'cdefgi', 'cdefhi', 'cdeghi', 'cdfghi', 'cefghi', 'defghi', 'abcdefg', 'abcdefh', 'abcdefi', 'abcdegh',
#             'abcdegi', 'abcdehi', 'abcdfgh', 'abcdfgi', 'abcdfhi', 'abcdghi', 'abcefgh', 'abcefgi', 'abcefhi',
#             'abceghi', 'abcfghi', 'abdefgh', 'abdefgi', 'abdefhi', 'abdeghi', 'abdfghi', 'abefghi', 'acdefgh',
#             'acdefgi', 'acdefhi', 'acdeghi', 'acdfghi', 'acefghi', 'adefghi', 'bcdefgh', 'bcdefgi', 'bcdefhi',
#             'bcdeghi', 'bcdfghi', 'bcefghi', 'bdefghi', 'cdefghi', 'abcdefgh', 'abcdefgi', 'abcdefhi', 'abcdeghi',
#             'abcdfghi', 'abcefghi', 'abdefghi', 'acdefghi', 'bcdefghi', 'abcdefghi']
#
# list1 = []
# for x, value in enumerate(powerset):
#     arr = [1, 'false', 'false', 'false', 'false', 'false', 'false', 'false', 'false', 'false', ]
#     for i, c in enumerate(value):
#         arr[0] = x + 1
#         if c == 'a':
#             arr[1] = 'true'
#         if c == 'b':
#             arr[2] = 'true'
#         if c == 'c':
#             arr[3] = 'true'
#         if c == 'd':
#             arr[4] = 'true'
#         if c == 'e':
#             arr[5] = 'true'
#         if c == 'f':
#             arr[6] = 'true'
#         if c == 'g':
#             arr[7] = 'true'
#         if c == 'h':
#             arr[8] = 'true'
#         if c == 'i':
#             arr[9] = 'true'
#     list1.append(arr)
#     print(x + 1)
#
# numbers = []
# for i in range(511):
#     numbers.append(i + 1)
#
# print(numbers)
#
# dicts = dict(zip(powerset, numbers))
# print(dicts)
#
# with open('output.csv', 'w') as f:
#     for _list in list1:
#         f.write('(')
#         for x, _string in enumerate(_list):
#             # f.seek(0)
#             if x == len(_list) - 1:
#                 f.write(str(_string))
#             else:
#                 f.write(str(_string) + ', ')
#         f.write('),' + '\n')

stringtoID = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'ab': 10, 'ac': 11, 'ad': 12,
              'ae': 13, 'af': 14, 'ag': 15, 'ah': 16, 'ai': 17, 'bc': 18, 'bd': 19, 'be': 20, 'bf': 21, 'bg': 22,
              'bh': 23,
              'bi': 24, 'cd': 25, 'ce': 26, 'cf': 27, 'cg': 28, 'ch': 29, 'ci': 30, 'de': 31, 'df': 32, 'dg': 33,
              'dh': 34,
              'di': 35, 'ef': 36, 'eg': 37, 'eh': 38, 'ei': 39, 'fg': 40, 'fh': 41, 'fi': 42, 'gh': 43, 'gi': 44,
              'hi': 45,
              'abc': 46, 'abd': 47, 'abe': 48, 'abf': 49, 'abg': 50, 'abh': 51, 'abi': 52, 'acd': 53, 'ace': 54,
              'acf': 55,
              'acg': 56, 'ach': 57, 'aci': 58, 'ade': 59, 'adf': 60, 'adg': 61, 'adh': 62, 'adi': 63, 'aef': 64,
              'aeg': 65,
              'aeh': 66, 'aei': 67, 'afg': 68, 'afh': 69, 'afi': 70, 'agh': 71, 'agi': 72, 'ahi': 73, 'bcd': 74,
              'bce': 75,
              'bcf': 76, 'bcg': 77, 'bch': 78, 'bci': 79, 'bde': 80, 'bdf': 81, 'bdg': 82, 'bdh': 83, 'bdi': 84,
              'bef': 85,
              'beg': 86, 'beh': 87, 'bei': 88, 'bfg': 89, 'bfh': 90, 'bfi': 91, 'bgh': 92, 'bgi': 93, 'bhi': 94,
              'cde': 95,
              'cdf': 96, 'cdg': 97, 'cdh': 98, 'cdi': 99, 'cef': 100, 'ceg': 101, 'ceh': 102, 'cei': 103, 'cfg': 104,
              'cfh': 105, 'cfi': 106, 'cgh': 107, 'cgi': 108, 'chi': 109, 'def': 110, 'deg': 111, 'deh': 112,
              'dei': 113,
              'dfg': 114, 'dfh': 115, 'dfi': 116, 'dgh': 117, 'dgi': 118, 'dhi': 119, 'efg': 120, 'efh': 121,
              'efi': 122,
              'egh': 123, 'egi': 124, 'ehi': 125, 'fgh': 126, 'fgi': 127, 'fhi': 128, 'ghi': 129, 'abcd': 130,
              'abce': 131,
              'abcf': 132, 'abcg': 133, 'abch': 134, 'abci': 135, 'abde': 136, 'abdf': 137, 'abdg': 138, 'abdh': 139,
              'abdi': 140, 'abef': 141, 'abeg': 142, 'abeh': 143, 'abei': 144, 'abfg': 145, 'abfh': 146, 'abfi': 147,
              'abgh': 148, 'abgi': 149, 'abhi': 150, 'acde': 151, 'acdf': 152, 'acdg': 153, 'acdh': 154, 'acdi': 155,
              'acef': 156, 'aceg': 157, 'aceh': 158, 'acei': 159, 'acfg': 160, 'acfh': 161, 'acfi': 162, 'acgh': 163,
              'acgi': 164, 'achi': 165, 'adef': 166, 'adeg': 167, 'adeh': 168, 'adei': 169, 'adfg': 170, 'adfh': 171,
              'adfi': 172, 'adgh': 173, 'adgi': 174, 'adhi': 175, 'aefg': 176, 'aefh': 177, 'aefi': 178, 'aegh': 179,
              'aegi': 180, 'aehi': 181, 'afgh': 182, 'afgi': 183, 'afhi': 184, 'aghi': 185, 'bcde': 186, 'bcdf': 187,
              'bcdg': 188, 'bcdh': 189, 'bcdi': 190, 'bcef': 191, 'bceg': 192, 'bceh': 193, 'bcei': 194, 'bcfg': 195,
              'bcfh': 196, 'bcfi': 197, 'bcgh': 198, 'bcgi': 199, 'bchi': 200, 'bdef': 201, 'bdeg': 202, 'bdeh': 203,
              'bdei': 204, 'bdfg': 205, 'bdfh': 206, 'bdfi': 207, 'bdgh': 208, 'bdgi': 209, 'bdhi': 210, 'befg': 211,
              'befh': 212, 'befi': 213, 'begh': 214, 'begi': 215, 'behi': 216, 'bfgh': 217, 'bfgi': 218, 'bfhi': 219,
              'bghi': 220, 'cdef': 221, 'cdeg': 222, 'cdeh': 223, 'cdei': 224, 'cdfg': 225, 'cdfh': 226, 'cdfi': 227,
              'cdgh': 228, 'cdgi': 229, 'cdhi': 230, 'cefg': 231, 'cefh': 232, 'cefi': 233, 'cegh': 234, 'cegi': 235,
              'cehi': 236, 'cfgh': 237, 'cfgi': 238, 'cfhi': 239, 'cghi': 240, 'defg': 241, 'defh': 242, 'defi': 243,
              'degh': 244, 'degi': 245, 'dehi': 246, 'dfgh': 247, 'dfgi': 248, 'dfhi': 249, 'dghi': 250, 'efgh': 251,
              'efgi': 252, 'efhi': 253, 'eghi': 254, 'fghi': 255, 'abcde': 256, 'abcdf': 257, 'abcdg': 258,
              'abcdh': 259,
              'abcdi': 260, 'abcef': 261, 'abceg': 262, 'abceh': 263, 'abcei': 264, 'abcfg': 265, 'abcfh': 266,
              'abcfi': 267, 'abcgh': 268, 'abcgi': 269, 'abchi': 270, 'abdef': 271, 'abdeg': 272, 'abdeh': 273,
              'abdei': 274, 'abdfg': 275, 'abdfh': 276, 'abdfi': 277, 'abdgh': 278, 'abdgi': 279, 'abdhi': 280,
              'abefg': 281, 'abefh': 282, 'abefi': 283, 'abegh': 284, 'abegi': 285, 'abehi': 286, 'abfgh': 287,
              'abfgi': 288, 'abfhi': 289, 'abghi': 290, 'acdef': 291, 'acdeg': 292, 'acdeh': 293, 'acdei': 294,
              'acdfg': 295, 'acdfh': 296, 'acdfi': 297, 'acdgh': 298, 'acdgi': 299, 'acdhi': 300, 'acefg': 301,
              'acefh': 302, 'acefi': 303, 'acegh': 304, 'acegi': 305, 'acehi': 306, 'acfgh': 307, 'acfgi': 308,
              'acfhi': 309, 'acghi': 310, 'adefg': 311, 'adefh': 312, 'adefi': 313, 'adegh': 314, 'adegi': 315,
              'adehi': 316, 'adfgh': 317, 'adfgi': 318, 'adfhi': 319, 'adghi': 320, 'aefgh': 321, 'aefgi': 322,
              'aefhi': 323, 'aeghi': 324, 'afghi': 325, 'bcdef': 326, 'bcdeg': 327, 'bcdeh': 328, 'bcdei': 329,
              'bcdfg': 330, 'bcdfh': 331, 'bcdfi': 332, 'bcdgh': 333, 'bcdgi': 334, 'bcdhi': 335, 'bcefg': 336,
              'bcefh': 337, 'bcefi': 338, 'bcegh': 339, 'bcegi': 340, 'bcehi': 341, 'bcfgh': 342, 'bcfgi': 343,
              'bcfhi': 344, 'bcghi': 345, 'bdefg': 346, 'bdefh': 347, 'bdefi': 348, 'bdegh': 349, 'bdegi': 350,
              'bdehi': 351, 'bdfgh': 352, 'bdfgi': 353, 'bdfhi': 354, 'bdghi': 355, 'befgh': 356, 'befgi': 357,
              'befhi': 358, 'beghi': 359, 'bfghi': 360, 'cdefg': 361, 'cdefh': 362, 'cdefi': 363, 'cdegh': 364,
              'cdegi': 365, 'cdehi': 366, 'cdfgh': 367, 'cdfgi': 368, 'cdfhi': 369, 'cdghi': 370, 'cefgh': 371,
              'cefgi': 372, 'cefhi': 373, 'ceghi': 374, 'cfghi': 375, 'defgh': 376, 'defgi': 377, 'defhi': 378,
              'deghi': 379, 'dfghi': 380, 'efghi': 381, 'abcdef': 382, 'abcdeg': 383, 'abcdeh': 384, 'abcdei': 385,
              'abcdfg': 386, 'abcdfh': 387, 'abcdfi': 388, 'abcdgh': 389, 'abcdgi': 390, 'abcdhi': 391, 'abcefg': 392,
              'abcefh': 393, 'abcefi': 394, 'abcegh': 395, 'abcegi': 396, 'abcehi': 397, 'abcfgh': 398, 'abcfgi': 399,
              'abcfhi': 400, 'abcghi': 401, 'abdefg': 402, 'abdefh': 403, 'abdefi': 404, 'abdegh': 405, 'abdegi': 406,
              'abdehi': 407, 'abdfgh': 408, 'abdfgi': 409, 'abdfhi': 410, 'abdghi': 411, 'abefgh': 412, 'abefgi': 413,
              'abefhi': 414, 'abeghi': 415, 'abfghi': 416, 'acdefg': 417, 'acdefh': 418, 'acdefi': 419, 'acdegh': 420,
              'acdegi': 421, 'acdehi': 422, 'acdfgh': 423, 'acdfgi': 424, 'acdfhi': 425, 'acdghi': 426, 'acefgh': 427,
              'acefgi': 428, 'acefhi': 429, 'aceghi': 430, 'acfghi': 431, 'adefgh': 432, 'adefgi': 433, 'adefhi': 434,
              'adeghi': 435, 'adfghi': 436, 'aefghi': 437, 'bcdefg': 438, 'bcdefh': 439, 'bcdefi': 440, 'bcdegh': 441,
              'bcdegi': 442, 'bcdehi': 443, 'bcdfgh': 444, 'bcdfgi': 445, 'bcdfhi': 446, 'bcdghi': 447, 'bcefgh': 448,
              'bcefgi': 449, 'bcefhi': 450, 'bceghi': 451, 'bcfghi': 452, 'bdefgh': 453, 'bdefgi': 454, 'bdefhi': 455,
              'bdeghi': 456, 'bdfghi': 457, 'befghi': 458, 'cdefgh': 459, 'cdefgi': 460, 'cdefhi': 461, 'cdeghi': 462,
              'abcdegh': 469, 'abcdegi': 470, 'abcdehi': 471, 'abcdfgh': 472, 'abcdfgi': 473, 'abcdfhi': 474,
              'abcdghi': 475,
              'abcefgh': 476, 'abcefgi': 477, 'abcefhi': 478, 'abceghi': 479, 'abcfghi': 480, 'abdefgh': 481,
              'abdefgi': 482, 'abdefhi': 483, 'abdeghi': 484, 'abdfghi': 485, 'abefghi': 486, 'acdefgh': 487,
              'acdefgi': 488, 'acdefhi': 489, 'acdeghi': 490, 'acdfghi': 491, 'acefghi': 492, 'adefghi': 493,
              'bcdefgh': 494, 'bcdefgi': 495, 'bcdefhi': 496, 'bcdeghi': 497, 'bcdfghi': 498, 'bcefghi': 499,
              'bdefghi': 500, 'cdefghi': 501, 'abcdefgh': 502, 'abcdefgi': 503, 'abcdefhi': 504, 'abcdeghi': 505,
              'abcdfghi': 506, 'abcefghi': 507, 'abdefghi': 508, 'acdefghi': 509, 'bcdefghi': 510, 'abcdefghi': 511}

idToString = {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e', 6: 'f', 7: 'g', 8: 'h', 9: 'i', 10: 'ab', 11: 'ac', 12: 'ad',
              13: 'ae', 14: 'af', 15: 'ag', 16: 'ah', 17: 'ai', 18: 'bc', 19: 'bd', 20: 'be', 21: 'bf', 22: 'bg',
              23: 'bh', 24: 'bi', 25: 'cd', 26: 'ce', 27: 'cf', 28: 'cg', 29: 'ch', 30: 'ci', 31: 'de', 32: 'df',
              33: 'dg', 34: 'dh', 35: 'di', 36: 'ef', 37: 'eg', 38: 'eh', 39: 'ei', 40: 'fg', 41: 'fh', 42: 'fi',
              43: 'gh', 44: 'gi', 45: 'hi', 46: 'abc', 47: 'abd', 48: 'abe', 49: 'abf', 50: 'abg', 51: 'abh',
              52: 'abi', 53: 'acd', 54: 'ace', 55: 'acf', 56: 'acg', 57: 'ach', 58: 'aci', 59: 'ade', 60: 'adf',
              61: 'adg', 62: 'adh', 63: 'adi', 64: 'aef', 65: 'aeg', 66: 'aeh', 67: 'aei', 68: 'afg', 69: 'afh',
              70: 'afi', 71: 'agh', 72: 'agi', 73: 'ahi', 74: 'bcd', 75: 'bce', 76: 'bcf', 77: 'bcg', 78: 'bch',
              79: 'bci', 80: 'bde', 81: 'bdf', 82: 'bdg', 83: 'bdh', 84: 'bdi', 85: 'bef', 86: 'beg', 87: 'beh',
              88: 'bei', 89: 'bfg', 90: 'bfh', 91: 'bfi', 92: 'bgh', 93: 'bgi', 94: 'bhi', 95: 'cde', 96: 'cdf',
              97: 'cdg', 98: 'cdh', 99: 'cdi', 100: 'cef', 101: 'ceg', 102: 'ceh', 103: 'cei', 104: 'cfg', 105: 'cfh',
              106: 'cfi', 107: 'cgh', 108: 'cgi', 109: 'chi', 110: 'def', 111: 'deg', 112: 'deh', 113: 'dei',
              114: 'dfg', 115: 'dfh', 116: 'dfi', 117: 'dgh', 118: 'dgi', 119: 'dhi', 120: 'efg', 121: 'efh',
              122: 'efi', 123: 'egh', 124: 'egi', 125: 'ehi', 126: 'fgh', 127: 'fgi', 128: 'fhi', 129: 'ghi',
              130: 'abcd', 131: 'abce', 132: 'abcf', 133: 'abcg', 134: 'abch', 135: 'abci', 136: 'abde', 137: 'abdf',
              138: 'abdg', 139: 'abdh', 140: 'abdi', 141: 'abef', 142: 'abeg', 143: 'abeh', 144: 'abei', 145: 'abfg',
              146: 'abfh', 147: 'abfi', 148: 'abgh', 149: 'abgi', 150: 'abhi', 151: 'acde', 152: 'acdf', 153: 'acdg',
              154: 'acdh', 155: 'acdi', 156: 'acef', 157: 'aceg', 158: 'aceh', 159: 'acei', 160: 'acfg', 161: 'acfh',
              162: 'acfi', 163: 'acgh', 164: 'acgi', 165: 'achi', 166: 'adef', 167: 'adeg', 168: 'adeh', 169: 'adei',
              170: 'adfg', 171: 'adfh', 172: 'adfi', 173: 'adgh', 174: 'adgi', 175: 'adhi', 176: 'aefg', 177: 'aefh',
              178: 'aefi', 179: 'aegh', 180: 'aegi', 181: 'aehi', 182: 'afgh', 183: 'afgi', 184: 'afhi', 185: 'aghi',
              186: 'bcde', 187: 'bcdf', 188: 'bcdg', 189: 'bcdh', 190: 'bcdi', 191: 'bcef', 192: 'bceg', 193: 'bceh',
              194: 'bcei', 195: 'bcfg', 196: 'bcfh', 197: 'bcfi', 198: 'bcgh', 199: 'bcgi', 200: 'bchi', 201: 'bdef',
              202: 'bdeg', 203: 'bdeh', 204: 'bdei', 205: 'bdfg', 206: 'bdfh', 207: 'bdfi', 208: 'bdgh', 209: 'bdgi',
              210: 'bdhi', 211: 'befg', 212: 'befh', 213: 'befi', 214: 'begh', 215: 'begi', 216: 'behi', 217: 'bfgh',
              218: 'bfgi', 219: 'bfhi', 220: 'bghi', 221: 'cdef', 222: 'cdeg', 223: 'cdeh', 224: 'cdei', 225: 'cdfg',
              226: 'cdfh', 227: 'cdfi', 228: 'cdgh', 229: 'cdgi', 230: 'cdhi', 231: 'cefg', 232: 'cefh', 233: 'cefi',
              234: 'cegh', 235: 'cegi', 236: 'cehi', 237: 'cfgh', 238: 'cfgi', 239: 'cfhi', 240: 'cghi', 241: 'defg',
              242: 'defh', 243: 'defi', 244: 'degh', 245: 'degi', 246: 'dehi', 247: 'dfgh', 248: 'dfgi', 249: 'dfhi',
              250: 'dghi', 251: 'efgh', 252: 'efgi', 253: 'efhi', 254: 'eghi', 255: 'fghi', 256: 'abcde', 257: 'abcdf',
              258: 'abcdg', 259: 'abcdh', 260: 'abcdi', 261: 'abcef', 262: 'abceg', 263: 'abceh', 264: 'abcei',
              265: 'abcfg', 266: 'abcfh', 267: 'abcfi', 268: 'abcgh', 269: 'abcgi', 270: 'abchi', 271: 'abdef',
              272: 'abdeg', 273: 'abdeh', 274: 'abdei', 275: 'abdfg', 276: 'abdfh', 277: 'abdfi', 278: 'abdgh',
              279: 'abdgi', 280: 'abdhi', 281: 'abefg', 282: 'abefh', 283: 'abefi', 284: 'abegh', 285: 'abegi',
              286: 'abehi', 287: 'abfgh', 288: 'abfgi', 289: 'abfhi', 290: 'abghi', 291: 'acdef', 292: 'acdeg',
              293: 'acdeh', 294: 'acdei', 295: 'acdfg', 296: 'acdfh', 297: 'acdfi', 298: 'acdgh', 299: 'acdgi',
              300: 'acdhi', 301: 'acefg', 302: 'acefh', 303: 'acefi', 304: 'acegh', 305: 'acegi', 306: 'acehi',
              307: 'acfgh', 308: 'acfgi', 309: 'acfhi', 310: 'acghi', 311: 'adefg', 312: 'adefh', 313: 'adefi',
              314: 'adegh', 315: 'adegi', 316: 'adehi', 317: 'adfgh', 318: 'adfgi', 319: 'adfhi', 320: 'adghi',
              321: 'aefgh', 322: 'aefgi', 323: 'aefhi', 324: 'aeghi', 325: 'afghi', 326: 'bcdef', 327: 'bcdeg',
              328: 'bcdeh', 329: 'bcdei', 330: 'bcdfg', 331: 'bcdfh', 332: 'bcdfi', 333: 'bcdgh', 334: 'bcdgi',
              335: 'bcdhi', 336: 'bcefg', 337: 'bcefh', 338: 'bcefi', 339: 'bcegh', 340: 'bcegi', 341: 'bcehi',
              342: 'bcfgh', 343: 'bcfgi', 344: 'bcfhi', 345: 'bcghi', 346: 'bdefg', 347: 'bdefh', 348: 'bdefi',
              349: 'bdegh', 350: 'bdegi', 351: 'bdehi', 352: 'bdfgh', 353: 'bdfgi', 354: 'bdfhi', 355: 'bdghi',
              356: 'befgh', 357: 'befgi', 358: 'befhi', 359: 'beghi', 360: 'bfghi', 361: 'cdefg', 362: 'cdefh',
              363: 'cdefi', 364: 'cdegh', 365: 'cdegi', 366: 'cdehi', 367: 'cdfgh', 368: 'cdfgi', 369: 'cdfhi',
              370: 'cdghi', 371: 'cefgh', 372: 'cefgi', 373: 'cefhi', 374: 'ceghi', 375: 'cfghi', 376: 'defgh',
              377: 'defgi', 378: 'defhi', 379: 'deghi', 380: 'dfghi', 381: 'efghi', 382: 'abcdef', 383: 'abcdeg',
              384: 'abcdeh', 385: 'abcdei', 386: 'abcdfg', 387: 'abcdfh', 388: 'abcdfi', 389: 'abcdgh', 390: 'abcdgi',
              391: 'abcdhi', 392: 'abcefg', 393: 'abcefh', 394: 'abcefi', 395: 'abcegh', 396: 'abcegi', 397: 'abcehi',
              398: 'abcfgh', 399: 'abcfgi', 400: 'abcfhi', 401: 'abcghi', 402: 'abdefg', 403: 'abdefh', 404: 'abdefi',
              405: 'abdegh', 406: 'abdegi', 407: 'abdehi', 408: 'abdfgh', 409: 'abdfgi', 410: 'abdfhi', 411: 'abdghi',
              412: 'abefgh', 413: 'abefgi', 414: 'abefhi', 415: 'abeghi', 416: 'abfghi', 417: 'acdefg', 418: 'acdefh',
              419: 'acdefi', 420: 'acdegh', 421: 'acdegi', 422: 'acdehi', 423: 'acdfgh', 424: 'acdfgi', 425: 'acdfhi',
              426: 'acdghi', 427: 'acefgh', 428: 'acefgi', 429: 'acefhi', 430: 'aceghi', 431: 'acfghi', 432: 'adefgh',
              433: 'adefgi', 434: 'adefhi', 435: 'adeghi', 436: 'adfghi', 437: 'aefghi', 438: 'bcdefg', 439: 'bcdefh',
              440: 'bcdefi', 441: 'bcdegh', 442: 'bcdegi', 443: 'bcdehi', 444: 'bcdfgh', 445: 'bcdfgi', 446: 'bcdfhi',
              447: 'bcdghi', 448: 'bcefgh', 449: 'bcefgi', 450: 'bcefhi', 451: 'bceghi', 452: 'bcfghi', 453: 'bdefgh',
              454: 'bdefgi', 455: 'bdefhi', 456: 'bdeghi', 457: 'bdfghi', 458: 'befghi', 459: 'cdefgh', 460: 'cdefgi',
              461: 'cdefhi', 462: 'cdeghi', 463: 'cdfghi', 464: 'cefghi', 465: 'defghi', 466: 'abcdefg',
              467: 'abcdefh', 468: 'abcdefi', 469: 'abcdegh', 470: 'abcdegi', 471: 'abcdehi', 472: 'abcdfgh',
              473: 'abcdfgi', 474: 'abcdfhi', 475: 'abcdghi', 476: 'abcefgh', 477: 'abcefgi', 478: 'abcefhi',
              479: 'abceghi', 480: 'abcfghi', 481: 'abdefgh', 482: 'abdefgi', 483: 'abdefhi', 484: 'abdeghi',
              485: 'abdfghi', 486: 'abefghi', 487: 'acdefgh', 488: 'acdefgi', 489: 'acdefhi', 490: 'acdeghi',
              491: 'acdfghi', 492: 'acefghi', 493: 'adefghi', 494: 'bcdefgh', 495: 'bcdefgi', 496: 'bcdefhi',
              497: 'bcdeghi', 498: 'bcdfghi', 499: 'bcefghi', 500: 'bdefghi', 501: 'cdefghi', 502: 'abcdefgh',
              503: 'abcdefgi', 504: 'abcdefhi', 505: 'abcdeghi', 506: 'abcdfghi', 507: 'abcefghi', 508: 'abdefghi',
              509: 'acdefghi', 510: 'bcdefghi', 511: 'abcdefghi'}


def getid(options):
    options = ''.join(options)
    value = stringtoID.get(options)
    return value


def getstring(id):
    value = idToString.get(int(id))
    value = list(value)
    return value
