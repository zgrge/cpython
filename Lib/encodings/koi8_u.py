""" Python Character Mapping Codec generated from 'python-mappings/KOI8-U.TXT' with gencodec.py.

"""#"

import codecs

### Codec APIs

class Codec(codecs.Codec):

    def encode(self,input,errors='strict'):

        return codecs.charmap_encode(input,errors,encoding_map)

    def decode(self,input,errors='strict'):

        return codecs.charmap_decode(input,errors,decoding_table)
    
class StreamWriter(Codec,codecs.StreamWriter):
    pass

class StreamReader(Codec,codecs.StreamReader):
    pass

### encodings module API

def getregentry():

    return (Codec().encode,Codec().decode,StreamReader,StreamWriter)


### Decoding Table

decoding_table = (
    u'\x00'	#  0x00 -> NULL
    u'\x01'	#  0x01 -> START OF HEADING
    u'\x02'	#  0x02 -> START OF TEXT
    u'\x03'	#  0x03 -> END OF TEXT
    u'\x04'	#  0x04 -> END OF TRANSMISSION
    u'\x05'	#  0x05 -> ENQUIRY
    u'\x06'	#  0x06 -> ACKNOWLEDGE
    u'\x07'	#  0x07 -> BELL
    u'\x08'	#  0x08 -> BACKSPACE
    u'\t'	#  0x09 -> HORIZONTAL TABULATION
    u'\n'	#  0x0a -> LINE FEED
    u'\x0b'	#  0x0b -> VERTICAL TABULATION
    u'\x0c'	#  0x0c -> FORM FEED
    u'\r'	#  0x0d -> CARRIAGE RETURN
    u'\x0e'	#  0x0e -> SHIFT OUT
    u'\x0f'	#  0x0f -> SHIFT IN
    u'\x10'	#  0x10 -> DATA LINK ESCAPE
    u'\x11'	#  0x11 -> DEVICE CONTROL ONE
    u'\x12'	#  0x12 -> DEVICE CONTROL TWO
    u'\x13'	#  0x13 -> DEVICE CONTROL THREE
    u'\x14'	#  0x14 -> DEVICE CONTROL FOUR
    u'\x15'	#  0x15 -> NEGATIVE ACKNOWLEDGE
    u'\x16'	#  0x16 -> SYNCHRONOUS IDLE
    u'\x17'	#  0x17 -> END OF TRANSMISSION BLOCK
    u'\x18'	#  0x18 -> CANCEL
    u'\x19'	#  0x19 -> END OF MEDIUM
    u'\x1a'	#  0x1a -> SUBSTITUTE
    u'\x1b'	#  0x1b -> ESCAPE
    u'\x1c'	#  0x1c -> FILE SEPARATOR
    u'\x1d'	#  0x1d -> GROUP SEPARATOR
    u'\x1e'	#  0x1e -> RECORD SEPARATOR
    u'\x1f'	#  0x1f -> UNIT SEPARATOR
    u' '	#  0x20 -> SPACE
    u'!'	#  0x21 -> EXCLAMATION MARK
    u'"'	#  0x22 -> QUOTATION MARK
    u'#'	#  0x23 -> NUMBER SIGN
    u'$'	#  0x24 -> DOLLAR SIGN
    u'%'	#  0x25 -> PERCENT SIGN
    u'&'	#  0x26 -> AMPERSAND
    u"'"	#  0x27 -> APOSTROPHE
    u'('	#  0x28 -> LEFT PARENTHESIS
    u')'	#  0x29 -> RIGHT PARENTHESIS
    u'*'	#  0x2a -> ASTERISK
    u'+'	#  0x2b -> PLUS SIGN
    u','	#  0x2c -> COMMA
    u'-'	#  0x2d -> HYPHEN-MINUS
    u'.'	#  0x2e -> FULL STOP
    u'/'	#  0x2f -> SOLIDUS
    u'0'	#  0x30 -> DIGIT ZERO
    u'1'	#  0x31 -> DIGIT ONE
    u'2'	#  0x32 -> DIGIT TWO
    u'3'	#  0x33 -> DIGIT THREE
    u'4'	#  0x34 -> DIGIT FOUR
    u'5'	#  0x35 -> DIGIT FIVE
    u'6'	#  0x36 -> DIGIT SIX
    u'7'	#  0x37 -> DIGIT SEVEN
    u'8'	#  0x38 -> DIGIT EIGHT
    u'9'	#  0x39 -> DIGIT NINE
    u':'	#  0x3a -> COLON
    u';'	#  0x3b -> SEMICOLON
    u'<'	#  0x3c -> LESS-THAN SIGN
    u'='	#  0x3d -> EQUALS SIGN
    u'>'	#  0x3e -> GREATER-THAN SIGN
    u'?'	#  0x3f -> QUESTION MARK
    u'@'	#  0x40 -> COMMERCIAL AT
    u'A'	#  0x41 -> LATIN CAPITAL LETTER A
    u'B'	#  0x42 -> LATIN CAPITAL LETTER B
    u'C'	#  0x43 -> LATIN CAPITAL LETTER C
    u'D'	#  0x44 -> LATIN CAPITAL LETTER D
    u'E'	#  0x45 -> LATIN CAPITAL LETTER E
    u'F'	#  0x46 -> LATIN CAPITAL LETTER F
    u'G'	#  0x47 -> LATIN CAPITAL LETTER G
    u'H'	#  0x48 -> LATIN CAPITAL LETTER H
    u'I'	#  0x49 -> LATIN CAPITAL LETTER I
    u'J'	#  0x4a -> LATIN CAPITAL LETTER J
    u'K'	#  0x4b -> LATIN CAPITAL LETTER K
    u'L'	#  0x4c -> LATIN CAPITAL LETTER L
    u'M'	#  0x4d -> LATIN CAPITAL LETTER M
    u'N'	#  0x4e -> LATIN CAPITAL LETTER N
    u'O'	#  0x4f -> LATIN CAPITAL LETTER O
    u'P'	#  0x50 -> LATIN CAPITAL LETTER P
    u'Q'	#  0x51 -> LATIN CAPITAL LETTER Q
    u'R'	#  0x52 -> LATIN CAPITAL LETTER R
    u'S'	#  0x53 -> LATIN CAPITAL LETTER S
    u'T'	#  0x54 -> LATIN CAPITAL LETTER T
    u'U'	#  0x55 -> LATIN CAPITAL LETTER U
    u'V'	#  0x56 -> LATIN CAPITAL LETTER V
    u'W'	#  0x57 -> LATIN CAPITAL LETTER W
    u'X'	#  0x58 -> LATIN CAPITAL LETTER X
    u'Y'	#  0x59 -> LATIN CAPITAL LETTER Y
    u'Z'	#  0x5a -> LATIN CAPITAL LETTER Z
    u'['	#  0x5b -> LEFT SQUARE BRACKET
    u'\\'	#  0x5c -> REVERSE SOLIDUS
    u']'	#  0x5d -> RIGHT SQUARE BRACKET
    u'^'	#  0x5e -> CIRCUMFLEX ACCENT
    u'_'	#  0x5f -> LOW LINE
    u'`'	#  0x60 -> GRAVE ACCENT
    u'a'	#  0x61 -> LATIN SMALL LETTER A
    u'b'	#  0x62 -> LATIN SMALL LETTER B
    u'c'	#  0x63 -> LATIN SMALL LETTER C
    u'd'	#  0x64 -> LATIN SMALL LETTER D
    u'e'	#  0x65 -> LATIN SMALL LETTER E
    u'f'	#  0x66 -> LATIN SMALL LETTER F
    u'g'	#  0x67 -> LATIN SMALL LETTER G
    u'h'	#  0x68 -> LATIN SMALL LETTER H
    u'i'	#  0x69 -> LATIN SMALL LETTER I
    u'j'	#  0x6a -> LATIN SMALL LETTER J
    u'k'	#  0x6b -> LATIN SMALL LETTER K
    u'l'	#  0x6c -> LATIN SMALL LETTER L
    u'm'	#  0x6d -> LATIN SMALL LETTER M
    u'n'	#  0x6e -> LATIN SMALL LETTER N
    u'o'	#  0x6f -> LATIN SMALL LETTER O
    u'p'	#  0x70 -> LATIN SMALL LETTER P
    u'q'	#  0x71 -> LATIN SMALL LETTER Q
    u'r'	#  0x72 -> LATIN SMALL LETTER R
    u's'	#  0x73 -> LATIN SMALL LETTER S
    u't'	#  0x74 -> LATIN SMALL LETTER T
    u'u'	#  0x75 -> LATIN SMALL LETTER U
    u'v'	#  0x76 -> LATIN SMALL LETTER V
    u'w'	#  0x77 -> LATIN SMALL LETTER W
    u'x'	#  0x78 -> LATIN SMALL LETTER X
    u'y'	#  0x79 -> LATIN SMALL LETTER Y
    u'z'	#  0x7a -> LATIN SMALL LETTER Z
    u'{'	#  0x7b -> LEFT CURLY BRACKET
    u'|'	#  0x7c -> VERTICAL LINE
    u'}'	#  0x7d -> RIGHT CURLY BRACKET
    u'~'	#  0x7e -> TILDE
    u'\x7f'	#  0x7f -> DELETE
    u'\u2500'	#  0x80 -> BOX DRAWINGS LIGHT HORIZONTAL
    u'\u2502'	#  0x81 -> BOX DRAWINGS LIGHT VERTICAL
    u'\u250c'	#  0x82 -> BOX DRAWINGS LIGHT DOWN AND RIGHT
    u'\u2510'	#  0x83 -> BOX DRAWINGS LIGHT DOWN AND LEFT
    u'\u2514'	#  0x84 -> BOX DRAWINGS LIGHT UP AND RIGHT
    u'\u2518'	#  0x85 -> BOX DRAWINGS LIGHT UP AND LEFT
    u'\u251c'	#  0x86 -> BOX DRAWINGS LIGHT VERTICAL AND RIGHT
    u'\u2524'	#  0x87 -> BOX DRAWINGS LIGHT VERTICAL AND LEFT
    u'\u252c'	#  0x88 -> BOX DRAWINGS LIGHT DOWN AND HORIZONTAL
    u'\u2534'	#  0x89 -> BOX DRAWINGS LIGHT UP AND HORIZONTAL
    u'\u253c'	#  0x8a -> BOX DRAWINGS LIGHT VERTICAL AND HORIZONTAL
    u'\u2580'	#  0x8b -> UPPER HALF BLOCK
    u'\u2584'	#  0x8c -> LOWER HALF BLOCK
    u'\u2588'	#  0x8d -> FULL BLOCK
    u'\u258c'	#  0x8e -> LEFT HALF BLOCK
    u'\u2590'	#  0x8f -> RIGHT HALF BLOCK
    u'\u2591'	#  0x90 -> LIGHT SHADE
    u'\u2592'	#  0x91 -> MEDIUM SHADE
    u'\u2593'	#  0x92 -> DARK SHADE
    u'\u2320'	#  0x93 -> TOP HALF INTEGRAL
    u'\u25a0'	#  0x94 -> BLACK SQUARE
    u'\u2219'	#  0x95 -> BULLET OPERATOR
    u'\u221a'	#  0x96 -> SQUARE ROOT
    u'\u2248'	#  0x97 -> ALMOST EQUAL TO
    u'\u2264'	#  0x98 -> LESS-THAN OR EQUAL TO
    u'\u2265'	#  0x99 -> GREATER-THAN OR EQUAL TO
    u'\xa0'	#  0x9a -> NO-BREAK SPACE
    u'\u2321'	#  0x9b -> BOTTOM HALF INTEGRAL
    u'\xb0'	#  0x9c -> DEGREE SIGN
    u'\xb2'	#  0x9d -> SUPERSCRIPT TWO
    u'\xb7'	#  0x9e -> MIDDLE DOT
    u'\xf7'	#  0x9f -> DIVISION SIGN
    u'\u2550'	#  0xa0 -> BOX DRAWINGS DOUBLE HORIZONTAL
    u'\u2551'	#  0xa1 -> BOX DRAWINGS DOUBLE VERTICAL
    u'\u2552'	#  0xa2 -> BOX DRAWINGS DOWN SINGLE AND RIGHT DOUBLE
    u'\u0451'	#  0xa3 -> CYRILLIC SMALL LETTER IO
    u'\u0454'	#  0xa4 -> CYRILLIC SMALL LETTER UKRAINIAN IE
    u'\u2554'	#  0xa5 -> BOX DRAWINGS DOUBLE DOWN AND RIGHT
    u'\u0456'	#  0xa6 -> CYRILLIC SMALL LETTER BYELORUSSIAN-UKRAINIAN I
    u'\u0457'	#  0xa7 -> CYRILLIC SMALL LETTER YI (UKRAINIAN)
    u'\u2557'	#  0xa8 -> BOX DRAWINGS DOUBLE DOWN AND LEFT
    u'\u2558'	#  0xa9 -> BOX DRAWINGS UP SINGLE AND RIGHT DOUBLE
    u'\u2559'	#  0xaa -> BOX DRAWINGS UP DOUBLE AND RIGHT SINGLE
    u'\u255a'	#  0xab -> BOX DRAWINGS DOUBLE UP AND RIGHT
    u'\u255b'	#  0xac -> BOX DRAWINGS UP SINGLE AND LEFT DOUBLE
    u'\u0491'	#  0xad -> CYRILLIC SMALL LETTER UKRAINIAN GHE WITH UPTURN
    u'\u255d'	#  0xae -> BOX DRAWINGS DOUBLE UP AND LEFT
    u'\u255e'	#  0xaf -> BOX DRAWINGS VERTICAL SINGLE AND RIGHT DOUBLE
    u'\u255f'	#  0xb0 -> BOX DRAWINGS VERTICAL DOUBLE AND RIGHT SINGLE
    u'\u2560'	#  0xb1 -> BOX DRAWINGS DOUBLE VERTICAL AND RIGHT
    u'\u2561'	#  0xb2 -> BOX DRAWINGS VERTICAL SINGLE AND LEFT DOUBLE
    u'\u0401'	#  0xb3 -> CYRILLIC CAPITAL LETTER IO
    u'\u0404'	#  0xb4 -> CYRILLIC CAPITAL LETTER UKRAINIAN IE
    u'\u2563'	#  0xb5 -> BOX DRAWINGS DOUBLE VERTICAL AND LEFT
    u'\u0406'	#  0xb6 -> CYRILLIC CAPITAL LETTER BYELORUSSIAN-UKRAINIAN I
    u'\u0407'	#  0xb7 -> CYRILLIC CAPITAL LETTER YI (UKRAINIAN)
    u'\u2566'	#  0xb8 -> BOX DRAWINGS DOUBLE DOWN AND HORIZONTAL
    u'\u2567'	#  0xb9 -> BOX DRAWINGS UP SINGLE AND HORIZONTAL DOUBLE
    u'\u2568'	#  0xba -> BOX DRAWINGS UP DOUBLE AND HORIZONTAL SINGLE
    u'\u2569'	#  0xbb -> BOX DRAWINGS DOUBLE UP AND HORIZONTAL
    u'\u256a'	#  0xbc -> BOX DRAWINGS VERTICAL SINGLE AND HORIZONTAL DOUBLE
    u'\u0490'	#  0xbd -> CYRILLIC CAPITAL LETTER UKRAINIAN GHE WITH UPTURN
    u'\u256c'	#  0xbe -> BOX DRAWINGS DOUBLE VERTICAL AND HORIZONTAL
    u'\xa9'	#  0xbf -> COPYRIGHT SIGN
    u'\u044e'	#  0xc0 -> CYRILLIC SMALL LETTER YU
    u'\u0430'	#  0xc1 -> CYRILLIC SMALL LETTER A
    u'\u0431'	#  0xc2 -> CYRILLIC SMALL LETTER BE
    u'\u0446'	#  0xc3 -> CYRILLIC SMALL LETTER TSE
    u'\u0434'	#  0xc4 -> CYRILLIC SMALL LETTER DE
    u'\u0435'	#  0xc5 -> CYRILLIC SMALL LETTER IE
    u'\u0444'	#  0xc6 -> CYRILLIC SMALL LETTER EF
    u'\u0433'	#  0xc7 -> CYRILLIC SMALL LETTER GHE
    u'\u0445'	#  0xc8 -> CYRILLIC SMALL LETTER HA
    u'\u0438'	#  0xc9 -> CYRILLIC SMALL LETTER I
    u'\u0439'	#  0xca -> CYRILLIC SMALL LETTER SHORT I
    u'\u043a'	#  0xcb -> CYRILLIC SMALL LETTER KA
    u'\u043b'	#  0xcc -> CYRILLIC SMALL LETTER EL
    u'\u043c'	#  0xcd -> CYRILLIC SMALL LETTER EM
    u'\u043d'	#  0xce -> CYRILLIC SMALL LETTER EN
    u'\u043e'	#  0xcf -> CYRILLIC SMALL LETTER O
    u'\u043f'	#  0xd0 -> CYRILLIC SMALL LETTER PE
    u'\u044f'	#  0xd1 -> CYRILLIC SMALL LETTER YA
    u'\u0440'	#  0xd2 -> CYRILLIC SMALL LETTER ER
    u'\u0441'	#  0xd3 -> CYRILLIC SMALL LETTER ES
    u'\u0442'	#  0xd4 -> CYRILLIC SMALL LETTER TE
    u'\u0443'	#  0xd5 -> CYRILLIC SMALL LETTER U
    u'\u0436'	#  0xd6 -> CYRILLIC SMALL LETTER ZHE
    u'\u0432'	#  0xd7 -> CYRILLIC SMALL LETTER VE
    u'\u044c'	#  0xd8 -> CYRILLIC SMALL LETTER SOFT SIGN
    u'\u044b'	#  0xd9 -> CYRILLIC SMALL LETTER YERU
    u'\u0437'	#  0xda -> CYRILLIC SMALL LETTER ZE
    u'\u0448'	#  0xdb -> CYRILLIC SMALL LETTER SHA
    u'\u044d'	#  0xdc -> CYRILLIC SMALL LETTER E
    u'\u0449'	#  0xdd -> CYRILLIC SMALL LETTER SHCHA
    u'\u0447'	#  0xde -> CYRILLIC SMALL LETTER CHE
    u'\u044a'	#  0xdf -> CYRILLIC SMALL LETTER HARD SIGN
    u'\u042e'	#  0xe0 -> CYRILLIC CAPITAL LETTER YU
    u'\u0410'	#  0xe1 -> CYRILLIC CAPITAL LETTER A
    u'\u0411'	#  0xe2 -> CYRILLIC CAPITAL LETTER BE
    u'\u0426'	#  0xe3 -> CYRILLIC CAPITAL LETTER TSE
    u'\u0414'	#  0xe4 -> CYRILLIC CAPITAL LETTER DE
    u'\u0415'	#  0xe5 -> CYRILLIC CAPITAL LETTER IE
    u'\u0424'	#  0xe6 -> CYRILLIC CAPITAL LETTER EF
    u'\u0413'	#  0xe7 -> CYRILLIC CAPITAL LETTER GHE
    u'\u0425'	#  0xe8 -> CYRILLIC CAPITAL LETTER HA
    u'\u0418'	#  0xe9 -> CYRILLIC CAPITAL LETTER I
    u'\u0419'	#  0xea -> CYRILLIC CAPITAL LETTER SHORT I
    u'\u041a'	#  0xeb -> CYRILLIC CAPITAL LETTER KA
    u'\u041b'	#  0xec -> CYRILLIC CAPITAL LETTER EL
    u'\u041c'	#  0xed -> CYRILLIC CAPITAL LETTER EM
    u'\u041d'	#  0xee -> CYRILLIC CAPITAL LETTER EN
    u'\u041e'	#  0xef -> CYRILLIC CAPITAL LETTER O
    u'\u041f'	#  0xf0 -> CYRILLIC CAPITAL LETTER PE
    u'\u042f'	#  0xf1 -> CYRILLIC CAPITAL LETTER YA
    u'\u0420'	#  0xf2 -> CYRILLIC CAPITAL LETTER ER
    u'\u0421'	#  0xf3 -> CYRILLIC CAPITAL LETTER ES
    u'\u0422'	#  0xf4 -> CYRILLIC CAPITAL LETTER TE
    u'\u0423'	#  0xf5 -> CYRILLIC CAPITAL LETTER U
    u'\u0416'	#  0xf6 -> CYRILLIC CAPITAL LETTER ZHE
    u'\u0412'	#  0xf7 -> CYRILLIC CAPITAL LETTER VE
    u'\u042c'	#  0xf8 -> CYRILLIC CAPITAL LETTER SOFT SIGN
    u'\u042b'	#  0xf9 -> CYRILLIC CAPITAL LETTER YERU
    u'\u0417'	#  0xfa -> CYRILLIC CAPITAL LETTER ZE
    u'\u0428'	#  0xfb -> CYRILLIC CAPITAL LETTER SHA
    u'\u042d'	#  0xfc -> CYRILLIC CAPITAL LETTER E
    u'\u0429'	#  0xfd -> CYRILLIC CAPITAL LETTER SHCHA
    u'\u0427'	#  0xfe -> CYRILLIC CAPITAL LETTER CHE
    u'\u042a'	#  0xff -> CYRILLIC CAPITAL LETTER HARD SIGN
)

### Encoding Map

encoding_map = {
    0x0000: 0x00,	#  NULL
    0x0001: 0x01,	#  START OF HEADING
    0x0002: 0x02,	#  START OF TEXT
    0x0003: 0x03,	#  END OF TEXT
    0x0004: 0x04,	#  END OF TRANSMISSION
    0x0005: 0x05,	#  ENQUIRY
    0x0006: 0x06,	#  ACKNOWLEDGE
    0x0007: 0x07,	#  BELL
    0x0008: 0x08,	#  BACKSPACE
    0x0009: 0x09,	#  HORIZONTAL TABULATION
    0x000a: 0x0a,	#  LINE FEED
    0x000b: 0x0b,	#  VERTICAL TABULATION
    0x000c: 0x0c,	#  FORM FEED
    0x000d: 0x0d,	#  CARRIAGE RETURN
    0x000e: 0x0e,	#  SHIFT OUT
    0x000f: 0x0f,	#  SHIFT IN
    0x0010: 0x10,	#  DATA LINK ESCAPE
    0x0011: 0x11,	#  DEVICE CONTROL ONE
    0x0012: 0x12,	#  DEVICE CONTROL TWO
    0x0013: 0x13,	#  DEVICE CONTROL THREE
    0x0014: 0x14,	#  DEVICE CONTROL FOUR
    0x0015: 0x15,	#  NEGATIVE ACKNOWLEDGE
    0x0016: 0x16,	#  SYNCHRONOUS IDLE
    0x0017: 0x17,	#  END OF TRANSMISSION BLOCK
    0x0018: 0x18,	#  CANCEL
    0x0019: 0x19,	#  END OF MEDIUM
    0x001a: 0x1a,	#  SUBSTITUTE
    0x001b: 0x1b,	#  ESCAPE
    0x001c: 0x1c,	#  FILE SEPARATOR
    0x001d: 0x1d,	#  GROUP SEPARATOR
    0x001e: 0x1e,	#  RECORD SEPARATOR
    0x001f: 0x1f,	#  UNIT SEPARATOR
    0x0020: 0x20,	#  SPACE
    0x0021: 0x21,	#  EXCLAMATION MARK
    0x0022: 0x22,	#  QUOTATION MARK
    0x0023: 0x23,	#  NUMBER SIGN
    0x0024: 0x24,	#  DOLLAR SIGN
    0x0025: 0x25,	#  PERCENT SIGN
    0x0026: 0x26,	#  AMPERSAND
    0x0027: 0x27,	#  APOSTROPHE
    0x0028: 0x28,	#  LEFT PARENTHESIS
    0x0029: 0x29,	#  RIGHT PARENTHESIS
    0x002a: 0x2a,	#  ASTERISK
    0x002b: 0x2b,	#  PLUS SIGN
    0x002c: 0x2c,	#  COMMA
    0x002d: 0x2d,	#  HYPHEN-MINUS
    0x002e: 0x2e,	#  FULL STOP
    0x002f: 0x2f,	#  SOLIDUS
    0x0030: 0x30,	#  DIGIT ZERO
    0x0031: 0x31,	#  DIGIT ONE
    0x0032: 0x32,	#  DIGIT TWO
    0x0033: 0x33,	#  DIGIT THREE
    0x0034: 0x34,	#  DIGIT FOUR
    0x0035: 0x35,	#  DIGIT FIVE
    0x0036: 0x36,	#  DIGIT SIX
    0x0037: 0x37,	#  DIGIT SEVEN
    0x0038: 0x38,	#  DIGIT EIGHT
    0x0039: 0x39,	#  DIGIT NINE
    0x003a: 0x3a,	#  COLON
    0x003b: 0x3b,	#  SEMICOLON
    0x003c: 0x3c,	#  LESS-THAN SIGN
    0x003d: 0x3d,	#  EQUALS SIGN
    0x003e: 0x3e,	#  GREATER-THAN SIGN
    0x003f: 0x3f,	#  QUESTION MARK
    0x0040: 0x40,	#  COMMERCIAL AT
    0x0041: 0x41,	#  LATIN CAPITAL LETTER A
    0x0042: 0x42,	#  LATIN CAPITAL LETTER B
    0x0043: 0x43,	#  LATIN CAPITAL LETTER C
    0x0044: 0x44,	#  LATIN CAPITAL LETTER D
    0x0045: 0x45,	#  LATIN CAPITAL LETTER E
    0x0046: 0x46,	#  LATIN CAPITAL LETTER F
    0x0047: 0x47,	#  LATIN CAPITAL LETTER G
    0x0048: 0x48,	#  LATIN CAPITAL LETTER H
    0x0049: 0x49,	#  LATIN CAPITAL LETTER I
    0x004a: 0x4a,	#  LATIN CAPITAL LETTER J
    0x004b: 0x4b,	#  LATIN CAPITAL LETTER K
    0x004c: 0x4c,	#  LATIN CAPITAL LETTER L
    0x004d: 0x4d,	#  LATIN CAPITAL LETTER M
    0x004e: 0x4e,	#  LATIN CAPITAL LETTER N
    0x004f: 0x4f,	#  LATIN CAPITAL LETTER O
    0x0050: 0x50,	#  LATIN CAPITAL LETTER P
    0x0051: 0x51,	#  LATIN CAPITAL LETTER Q
    0x0052: 0x52,	#  LATIN CAPITAL LETTER R
    0x0053: 0x53,	#  LATIN CAPITAL LETTER S
    0x0054: 0x54,	#  LATIN CAPITAL LETTER T
    0x0055: 0x55,	#  LATIN CAPITAL LETTER U
    0x0056: 0x56,	#  LATIN CAPITAL LETTER V
    0x0057: 0x57,	#  LATIN CAPITAL LETTER W
    0x0058: 0x58,	#  LATIN CAPITAL LETTER X
    0x0059: 0x59,	#  LATIN CAPITAL LETTER Y
    0x005a: 0x5a,	#  LATIN CAPITAL LETTER Z
    0x005b: 0x5b,	#  LEFT SQUARE BRACKET
    0x005c: 0x5c,	#  REVERSE SOLIDUS
    0x005d: 0x5d,	#  RIGHT SQUARE BRACKET
    0x005e: 0x5e,	#  CIRCUMFLEX ACCENT
    0x005f: 0x5f,	#  LOW LINE
    0x0060: 0x60,	#  GRAVE ACCENT
    0x0061: 0x61,	#  LATIN SMALL LETTER A
    0x0062: 0x62,	#  LATIN SMALL LETTER B
    0x0063: 0x63,	#  LATIN SMALL LETTER C
    0x0064: 0x64,	#  LATIN SMALL LETTER D
    0x0065: 0x65,	#  LATIN SMALL LETTER E
    0x0066: 0x66,	#  LATIN SMALL LETTER F
    0x0067: 0x67,	#  LATIN SMALL LETTER G
    0x0068: 0x68,	#  LATIN SMALL LETTER H
    0x0069: 0x69,	#  LATIN SMALL LETTER I
    0x006a: 0x6a,	#  LATIN SMALL LETTER J
    0x006b: 0x6b,	#  LATIN SMALL LETTER K
    0x006c: 0x6c,	#  LATIN SMALL LETTER L
    0x006d: 0x6d,	#  LATIN SMALL LETTER M
    0x006e: 0x6e,	#  LATIN SMALL LETTER N
    0x006f: 0x6f,	#  LATIN SMALL LETTER O
    0x0070: 0x70,	#  LATIN SMALL LETTER P
    0x0071: 0x71,	#  LATIN SMALL LETTER Q
    0x0072: 0x72,	#  LATIN SMALL LETTER R
    0x0073: 0x73,	#  LATIN SMALL LETTER S
    0x0074: 0x74,	#  LATIN SMALL LETTER T
    0x0075: 0x75,	#  LATIN SMALL LETTER U
    0x0076: 0x76,	#  LATIN SMALL LETTER V
    0x0077: 0x77,	#  LATIN SMALL LETTER W
    0x0078: 0x78,	#  LATIN SMALL LETTER X
    0x0079: 0x79,	#  LATIN SMALL LETTER Y
    0x007a: 0x7a,	#  LATIN SMALL LETTER Z
    0x007b: 0x7b,	#  LEFT CURLY BRACKET
    0x007c: 0x7c,	#  VERTICAL LINE
    0x007d: 0x7d,	#  RIGHT CURLY BRACKET
    0x007e: 0x7e,	#  TILDE
    0x007f: 0x7f,	#  DELETE
    0x00a0: 0x9a,	#  NO-BREAK SPACE
    0x00a9: 0xbf,	#  COPYRIGHT SIGN
    0x00b0: 0x9c,	#  DEGREE SIGN
    0x00b2: 0x9d,	#  SUPERSCRIPT TWO
    0x00b7: 0x9e,	#  MIDDLE DOT
    0x00f7: 0x9f,	#  DIVISION SIGN
    0x0401: 0xb3,	#  CYRILLIC CAPITAL LETTER IO
    0x0404: 0xb4,	#  CYRILLIC CAPITAL LETTER UKRAINIAN IE
    0x0406: 0xb6,	#  CYRILLIC CAPITAL LETTER BYELORUSSIAN-UKRAINIAN I
    0x0407: 0xb7,	#  CYRILLIC CAPITAL LETTER YI (UKRAINIAN)
    0x0410: 0xe1,	#  CYRILLIC CAPITAL LETTER A
    0x0411: 0xe2,	#  CYRILLIC CAPITAL LETTER BE
    0x0412: 0xf7,	#  CYRILLIC CAPITAL LETTER VE
    0x0413: 0xe7,	#  CYRILLIC CAPITAL LETTER GHE
    0x0414: 0xe4,	#  CYRILLIC CAPITAL LETTER DE
    0x0415: 0xe5,	#  CYRILLIC CAPITAL LETTER IE
    0x0416: 0xf6,	#  CYRILLIC CAPITAL LETTER ZHE
    0x0417: 0xfa,	#  CYRILLIC CAPITAL LETTER ZE
    0x0418: 0xe9,	#  CYRILLIC CAPITAL LETTER I
    0x0419: 0xea,	#  CYRILLIC CAPITAL LETTER SHORT I
    0x041a: 0xeb,	#  CYRILLIC CAPITAL LETTER KA
    0x041b: 0xec,	#  CYRILLIC CAPITAL LETTER EL
    0x041c: 0xed,	#  CYRILLIC CAPITAL LETTER EM
    0x041d: 0xee,	#  CYRILLIC CAPITAL LETTER EN
    0x041e: 0xef,	#  CYRILLIC CAPITAL LETTER O
    0x041f: 0xf0,	#  CYRILLIC CAPITAL LETTER PE
    0x0420: 0xf2,	#  CYRILLIC CAPITAL LETTER ER
    0x0421: 0xf3,	#  CYRILLIC CAPITAL LETTER ES
    0x0422: 0xf4,	#  CYRILLIC CAPITAL LETTER TE
    0x0423: 0xf5,	#  CYRILLIC CAPITAL LETTER U
    0x0424: 0xe6,	#  CYRILLIC CAPITAL LETTER EF
    0x0425: 0xe8,	#  CYRILLIC CAPITAL LETTER HA
    0x0426: 0xe3,	#  CYRILLIC CAPITAL LETTER TSE
    0x0427: 0xfe,	#  CYRILLIC CAPITAL LETTER CHE
    0x0428: 0xfb,	#  CYRILLIC CAPITAL LETTER SHA
    0x0429: 0xfd,	#  CYRILLIC CAPITAL LETTER SHCHA
    0x042a: 0xff,	#  CYRILLIC CAPITAL LETTER HARD SIGN
    0x042b: 0xf9,	#  CYRILLIC CAPITAL LETTER YERU
    0x042c: 0xf8,	#  CYRILLIC CAPITAL LETTER SOFT SIGN
    0x042d: 0xfc,	#  CYRILLIC CAPITAL LETTER E
    0x042e: 0xe0,	#  CYRILLIC CAPITAL LETTER YU
    0x042f: 0xf1,	#  CYRILLIC CAPITAL LETTER YA
    0x0430: 0xc1,	#  CYRILLIC SMALL LETTER A
    0x0431: 0xc2,	#  CYRILLIC SMALL LETTER BE
    0x0432: 0xd7,	#  CYRILLIC SMALL LETTER VE
    0x0433: 0xc7,	#  CYRILLIC SMALL LETTER GHE
    0x0434: 0xc4,	#  CYRILLIC SMALL LETTER DE
    0x0435: 0xc5,	#  CYRILLIC SMALL LETTER IE
    0x0436: 0xd6,	#  CYRILLIC SMALL LETTER ZHE
    0x0437: 0xda,	#  CYRILLIC SMALL LETTER ZE
    0x0438: 0xc9,	#  CYRILLIC SMALL LETTER I
    0x0439: 0xca,	#  CYRILLIC SMALL LETTER SHORT I
    0x043a: 0xcb,	#  CYRILLIC SMALL LETTER KA
    0x043b: 0xcc,	#  CYRILLIC SMALL LETTER EL
    0x043c: 0xcd,	#  CYRILLIC SMALL LETTER EM
    0x043d: 0xce,	#  CYRILLIC SMALL LETTER EN
    0x043e: 0xcf,	#  CYRILLIC SMALL LETTER O
    0x043f: 0xd0,	#  CYRILLIC SMALL LETTER PE
    0x0440: 0xd2,	#  CYRILLIC SMALL LETTER ER
    0x0441: 0xd3,	#  CYRILLIC SMALL LETTER ES
    0x0442: 0xd4,	#  CYRILLIC SMALL LETTER TE
    0x0443: 0xd5,	#  CYRILLIC SMALL LETTER U
    0x0444: 0xc6,	#  CYRILLIC SMALL LETTER EF
    0x0445: 0xc8,	#  CYRILLIC SMALL LETTER HA
    0x0446: 0xc3,	#  CYRILLIC SMALL LETTER TSE
    0x0447: 0xde,	#  CYRILLIC SMALL LETTER CHE
    0x0448: 0xdb,	#  CYRILLIC SMALL LETTER SHA
    0x0449: 0xdd,	#  CYRILLIC SMALL LETTER SHCHA
    0x044a: 0xdf,	#  CYRILLIC SMALL LETTER HARD SIGN
    0x044b: 0xd9,	#  CYRILLIC SMALL LETTER YERU
    0x044c: 0xd8,	#  CYRILLIC SMALL LETTER SOFT SIGN
    0x044d: 0xdc,	#  CYRILLIC SMALL LETTER E
    0x044e: 0xc0,	#  CYRILLIC SMALL LETTER YU
    0x044f: 0xd1,	#  CYRILLIC SMALL LETTER YA
    0x0451: 0xa3,	#  CYRILLIC SMALL LETTER IO
    0x0454: 0xa4,	#  CYRILLIC SMALL LETTER UKRAINIAN IE
    0x0456: 0xa6,	#  CYRILLIC SMALL LETTER BYELORUSSIAN-UKRAINIAN I
    0x0457: 0xa7,	#  CYRILLIC SMALL LETTER YI (UKRAINIAN)
    0x0490: 0xbd,	#  CYRILLIC CAPITAL LETTER UKRAINIAN GHE WITH UPTURN
    0x0491: 0xad,	#  CYRILLIC SMALL LETTER UKRAINIAN GHE WITH UPTURN
    0x2219: 0x95,	#  BULLET OPERATOR
    0x221a: 0x96,	#  SQUARE ROOT
    0x2248: 0x97,	#  ALMOST EQUAL TO
    0x2264: 0x98,	#  LESS-THAN OR EQUAL TO
    0x2265: 0x99,	#  GREATER-THAN OR EQUAL TO
    0x2320: 0x93,	#  TOP HALF INTEGRAL
    0x2321: 0x9b,	#  BOTTOM HALF INTEGRAL
    0x2500: 0x80,	#  BOX DRAWINGS LIGHT HORIZONTAL
    0x2502: 0x81,	#  BOX DRAWINGS LIGHT VERTICAL
    0x250c: 0x82,	#  BOX DRAWINGS LIGHT DOWN AND RIGHT
    0x2510: 0x83,	#  BOX DRAWINGS LIGHT DOWN AND LEFT
    0x2514: 0x84,	#  BOX DRAWINGS LIGHT UP AND RIGHT
    0x2518: 0x85,	#  BOX DRAWINGS LIGHT UP AND LEFT
    0x251c: 0x86,	#  BOX DRAWINGS LIGHT VERTICAL AND RIGHT
    0x2524: 0x87,	#  BOX DRAWINGS LIGHT VERTICAL AND LEFT
    0x252c: 0x88,	#  BOX DRAWINGS LIGHT DOWN AND HORIZONTAL
    0x2534: 0x89,	#  BOX DRAWINGS LIGHT UP AND HORIZONTAL
    0x253c: 0x8a,	#  BOX DRAWINGS LIGHT VERTICAL AND HORIZONTAL
    0x2550: 0xa0,	#  BOX DRAWINGS DOUBLE HORIZONTAL
    0x2551: 0xa1,	#  BOX DRAWINGS DOUBLE VERTICAL
    0x2552: 0xa2,	#  BOX DRAWINGS DOWN SINGLE AND RIGHT DOUBLE
    0x2554: 0xa5,	#  BOX DRAWINGS DOUBLE DOWN AND RIGHT
    0x2557: 0xa8,	#  BOX DRAWINGS DOUBLE DOWN AND LEFT
    0x2558: 0xa9,	#  BOX DRAWINGS UP SINGLE AND RIGHT DOUBLE
    0x2559: 0xaa,	#  BOX DRAWINGS UP DOUBLE AND RIGHT SINGLE
    0x255a: 0xab,	#  BOX DRAWINGS DOUBLE UP AND RIGHT
    0x255b: 0xac,	#  BOX DRAWINGS UP SINGLE AND LEFT DOUBLE
    0x255d: 0xae,	#  BOX DRAWINGS DOUBLE UP AND LEFT
    0x255e: 0xaf,	#  BOX DRAWINGS VERTICAL SINGLE AND RIGHT DOUBLE
    0x255f: 0xb0,	#  BOX DRAWINGS VERTICAL DOUBLE AND RIGHT SINGLE
    0x2560: 0xb1,	#  BOX DRAWINGS DOUBLE VERTICAL AND RIGHT
    0x2561: 0xb2,	#  BOX DRAWINGS VERTICAL SINGLE AND LEFT DOUBLE
    0x2563: 0xb5,	#  BOX DRAWINGS DOUBLE VERTICAL AND LEFT
    0x2566: 0xb8,	#  BOX DRAWINGS DOUBLE DOWN AND HORIZONTAL
    0x2567: 0xb9,	#  BOX DRAWINGS UP SINGLE AND HORIZONTAL DOUBLE
    0x2568: 0xba,	#  BOX DRAWINGS UP DOUBLE AND HORIZONTAL SINGLE
    0x2569: 0xbb,	#  BOX DRAWINGS DOUBLE UP AND HORIZONTAL
    0x256a: 0xbc,	#  BOX DRAWINGS VERTICAL SINGLE AND HORIZONTAL DOUBLE
    0x256c: 0xbe,	#  BOX DRAWINGS DOUBLE VERTICAL AND HORIZONTAL
    0x2580: 0x8b,	#  UPPER HALF BLOCK
    0x2584: 0x8c,	#  LOWER HALF BLOCK
    0x2588: 0x8d,	#  FULL BLOCK
    0x258c: 0x8e,	#  LEFT HALF BLOCK
    0x2590: 0x8f,	#  RIGHT HALF BLOCK
    0x2591: 0x90,	#  LIGHT SHADE
    0x2592: 0x91,	#  MEDIUM SHADE
    0x2593: 0x92,	#  DARK SHADE
    0x25a0: 0x94,	#  BLACK SQUARE
}