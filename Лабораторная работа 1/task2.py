# TODO Найдите количество книг, которое можно разместить на дискете
symbol = 4
stroka = 25 * symbol
straniza = stroka * 50
kniga = straniza * 100
disc = 1.44 * (2**20)
v = disc // kniga
print("Количество книг, помещающихся на дискету:", round(v))
