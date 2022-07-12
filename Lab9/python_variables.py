# TASK: calculate price with VAT (ДДС)
# base_prise = 100
# price_with_vat = base_prise * 1.2

# print( price_with_vat )

# 	# Global:
# 	# base_prise: 0x01213131
# 	# price_with_vat:0x98939398

# 	# RAM:
# 	#  0x01213131: 0101010101,  (100)
# 	#  0x98939398: 1011011111 (120)

# ----------------------------- Identifiers rules ---------------------------- #
# BasePrice = 100 # valid

# print( base_price )

# --------------------------------- examples --------------------------------- #
### example 1
# x = 5 + 5
# y = 9

# x = y+x

# print(x) # 19?

# # Global:
# # 	x: 0x658765
# # 	y: 0x894959


# # RAM:
# 	0x658765:1010101 (19)
# 	0x894959:0101010 (9)

### example2
# x = 5
# print( id(x) )

### name binding example
a = 3
b = a # copy by value
c = a # copy by value
a = "hi"
print(a)


#  a: 0x12 => (3)
#  b: 0x45 => (3)
#  c: 0x34 => (3)
