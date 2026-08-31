// primitivos.groovy

// Tipos primitivos "clássicos" da JVM (herdados do Java)
byte a = -12
short b = 1000
int c = 100_000
long d = 9_000_000_000L

float e = 3.14f
double f = 2.71828d

boolean g = true
char h = 'G'

println "byte: $a"
println "short: $b"
println "int: $c"
println "long: $d"
println "float: $e"
println "double: $f"
println "boolean: $g"
println "char: $h"

// Groovy também tem tipagem dinâmica com "def"
// Nesse caso, o tipo primitivo vira automaticamente um objeto (wrapper)
def i = 42          // vira Integer por baixo dos panos
def j = 3.14         // vira BigDecimal por padrão (não float/double!)

println "def i (${i.class}): $i"
println "def j (${j.class}): $j"