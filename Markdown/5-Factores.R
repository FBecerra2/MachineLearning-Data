### Factores

factor()
as,factor()
levels()

nombres= c("Juan","Antonio","Ricardo","Juan","Juan", "Maria","Maria")

nombres
nombres.factor = factor(nombres)
nombres.factor

gender = c("M","H","H","M","M","M","M","H","H")
gender.fact = factor(gender)
gender.fact
gender.fact2 = as.factor(gender)
gender.fact2
gender.fact3 = factor(gender, levels = c("M","H","B"))
gender.fact3
gender.fact4 = factor(gender,levels =c("M","H","B"), labels = c("Mujer","Hombre","Hermafrodita"))
gender.fact4
levels(gender.fact4)
levels(gender.fact4) = c("Femenino","Masculino","Hibrido")
gender.fact4


ordered(vector,levels=...)


notas = c(1,4,3,2,3,2,4,3,1,2,3,4,2,3,4)
notas
notas.fact = factor(notas)
notas.fact
ordered(notas, labels = c("Sus", "Suf", "Not", "Exc"))





