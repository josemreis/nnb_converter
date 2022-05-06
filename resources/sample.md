# 3 Types, Values, and Variables

Notebook for chapter 3 of [JavaScript: The Definitive Guide: Master the World's Most-Used Programming Language, 7th Edition](https://www.oreilly.com/library/view/javascript-the-definitive/9781491952016/).

JavaScript types can be divided into two categories: *primitive types* and *object types*. JavaScript's primitive types are composed by:
* text
* number
* boolean
* symbol
* `null`
* `undefined`

Any type which is not one of the described above is defined as *type object* or an `object`. An `object` is a collection of `properties`, where each property as a name and a value (either a primitive value or another object).

An ordinary object is an *unordered collection of named values*. However, there are special types of object which differ from these standard objects, such as:
* An `array` is an *ordered collection of numbered values*

```javascript
const fruits = ['Maçã', 'Banana'];

console.log(fruits);
```
```bash
## [ 'Maçã', 'Banana' ]
```

* A `Set` object represents a set of **unique** values

```javascript
const my_set1 = new Set()

my_set1.add(1)           // Set [ 1 ]
my_set1.add(5)           // Set [ 1, 5 ]
my_set1.add(5)           // Set [ 1, 5 ]
my_set1.add('some text') // Set [ 1, 5, 'some text' ]

console.log(my_set1)
```
```bash
## Set(3) { 1, 5, 'some text' }
```

* A `Map` object represents mapping keys to values (fairly similar, at least in usage, to Python's dictionaries)

```typescript
// this is a map
const fruits2 = new Map([
    ["apples", 500],
    ["bananas", 300],
    ["oranges", 200]
  ]);

  console.log(fruits2)
```
```bash
## Map(3) { 'apples' => 500, 'bananas' => 300, 'oranges' => 200 }
```

Among other...

## Numbers

`Number`, a primitive js numeric type, is used to represent integers and to approximate real numbers.

### Integer Literals

In a JavaScript program, a base-10 integer is written as a sequence of digits. For example:

```typescript
0
3
10000000
```
```bash
## [33m10000000[39m
```

In addition to base-10 integer literals, JavaScript recognizes hexadecimal (base-16) values. A hexadecimal literal begins with `0x` or `0X`, followed by a string of hexadecimal digits. A hexadecimal digit is one of the digits 0 through 9 or the letters a (or A)
through f (or F), which represent values 10 through 15. Here are examples of hexadecimal integer literals:

```typescript
a = 0xff// => 255: (15*16 + 15)
console.log(a)
b = 0xBADCAFE // => 195939070
console.log(b)
```
```bash
## 255
## 195939070
```

### Floating-Point Literals

Floating-point literals can have a decimal point; they use the traditional syntax for real numbers. A real value is represented as the integral part of the number, followed by a decimal point and the fractional part of the number.

```typescript
3.14
2345.6789
.333333333333333333
6.02e23
// 6.02 × 10²³
1.4738223E-32 // 1.4738223 × 10 ⁻ ³²
```
```bash
## [33m1.4738223e-32[39m
```

### Arithmetic in JavaScript

JavaScript programs work with numbers using the arithmetic operators . that the language provides. These include + for addition, - for subtraction, * for multiplication, / for division, and % for modulo (remainder after division). ES2016 adds ** for exponentiation. Full details on these and other operators can be found in Chapter 4.

```javascript
Math.pow(2,53) // => 9007199254740992: 2 to the power 53
Math.round(.6) // => 1.0: round to the nearest integer
Math.ceil(.6) // => 1.0: round up to an integer
Math.floor(.6) // => 0.0: round down to an integer
Math.abs(-5) // => 5: absolute value
Math.max(1,2,3) // Return the largest argument
Math.min(1,2,3) // Return the smallest argument
Math.random() // Pseudo-random number x where 0 <= x < 1.0
Math.PI // π: circumference of a circle / diameter
Math.E // e: The base of the natural logarithm
Math.sqrt(3) // => 3**0.5: the square root of 3
Math.pow(3, 1/3) // => 3**(1/3): the cube root of 3
Math.sin(0) // Trigonometry: also Math.cos, Math.atan, etc.
Math.log(10) // Natural logarithm of 10
Math.log(100)/Math.LN10 // Base 10 logarithm of 100
Math.cbrt(27) // => 3: cube root
Math.hypot(3, 4) // => 5: square root of sum of squares of all arguments
Math.log10(100) // ()=> 2: Base-10 logarithm
Math.log2(1024) // => 10: Base-2 logarithm
Math.log1p(x) // Natural log of (1+x); accurate for very small x
Math.expm1(x) // Math.exp(x)-1; the inverse of Math.log1p()
Math.sign(x) // -1, 0, or 1 for arguments <, ==, or > 0
Math.imul(2,3) // => 6: optimized multiplication of 32-bit integers
Math.clz32(0xf) // => 28: number of leading zero bits in a 32-bit integer
Math.trunc(3.9) // => 3: convert to an integer by truncating fractional part
Math.fround(x) // Round to nearest 32-bit float number
Math.sinh(x) // Hyperbolic sine. Also Math.cosh(), Math.tanh()
Math.asinh(x) // Hyperbolic arcsine. Also Math.acosh(), Math.atanh()








```
```bash
## [33mNaN[39m
```

Arithmetic in JavaScript does not raise errors in cases of overflow, underflow, or division by zero. When the result of a numeric operation is larger than the largest representable number (overflow), the result is a special infinity value, Infinity.

```javascript
Infinity
Number.POSITIVE_INFINITY
1/0
Number.MAX_VALUE * 2
-Infinity
Number.NEGATIVE_INFINITY
-1/0
-Number.MAX_VALUE * 2
NaN
Number.NaN
0/0
Infinity/Infinity
Number.MIN_VALUE/2
-Number.MIN_VALUE/2
-1/Infinity
-0
```
```bash
## [33m0[39m
```

The not-a-number value has one unusual feature in JavaScript: it does not compare equal to any other value, including itself. This means that you can’t write `x === NaN` to determine whether the value of a variable x is NaN. Instead, you must write `x != x`
or `Number.isNaN(x)`. Those expressions will be true if, and only if, x has the same value as the global constant NaN.

```javascript
x = NaN

test_1 = x == NaN

test_2 = Number.isNaN(x)


console.log(test_1)
console.log(test_2)
```
```bash
## false
## true
```

Related to this, the function `Number.isFinite()` evaluates if an argument is a `Number` other than `NaN`, `Infinity`, or `-Infinity`

```javascript
a = 1011
b = Infinity
c = NaN

console.log(Number.isFinite(a))
console.log(Number.isFinite(b))
console.log(Number.isFinite(c))
```
```bash
## true
## false
## false
```

### Arbitrary Precision Integers with BigInt

As the name implies, BigInt is a numeric type whose values are integers. The type was added to JavaScript mainly to allow the representation of 64-bit integers, which are required for compati‐
bility with many other programming languages and APIs. But BigInt values can have thousands or even millions of digits, should you have need to work with numbers that large. You can use BigInt() as a function for converting regular JavaScript numbers or
strings to BigInt values:

```javascript
largest_number_allowed = Number.MAX_SAFE_INTEGER

even_larger = Math.pow(largest_number_allowed, 2)

console.log(even_larger)

as_big_int = BigInt(even_larger)

console.log(as_big_int)
```
```bash
## 8.112963841460666e+31
## 81129638414606663681390495662080n
```

### Dates and Times

JavaScript defines a simple Date class for representing and manipulating the numbers that represent dates and times. JavaScript Dates are objects, but they also have a numeric representation as a timestamp that specifies the number of elapsed milliseconds since January 1, 1970:

```javascript
let timestamp = Date.now() // today's date as timestamp
console.log(timestamp)
let now = Date() // today's date as a Date object
console.log(now)
```
```bash
## 1651853407085
## Fri May 06 2022 17:10:07 GMT+0100 (Western European Summer Time)
```

The date methods will be covered in more detail later on. 

## Text

The JavaScript type for representing text is the *string*. A string is an immutable ordered sequence of 16-bit values, each of which typically representas a Unicode character. The *length* of a string is the number of 16-bit values it contains. JavaScript’s
strings (and its arrays) use zero-based indexing: the first 16-bit value is at position 0, the second at position 1, and so on. The empty string is the string of length 0. JavaScript does not have a special type that represents a single element of a string.

### String Literals

To include a string in a JavaScript program, simply enclose the characters of the string within a matched pair of single or double quotes or backticks ( ' or " or ` ). Double-quote characters and backticks may be contained within strings delimited by single-quote characters, and similarly for strings delimited by double quotes and backticks.

The original versions of JavaScript required string literals to be written on a single line, and it is common to see JavaScript code that creates long strings by concatenating single-line strings with the + operator. As of ES5, however, you can break a string literal across multiple lines by ending each line but the last with a backslash ( \ ).

```javascript
a_text = "Hello"
another_text = "World!"

console.log(a_text + another_text)
console.log(a_text + " " +  another_text)
console.log(a_text + "\n" +  another_text)
console.log(a_text  +  another_text)
```
```bash
## HelloWorld!
## Hello World!
## Hello
## World!
## HelloWorld!
```

The backslash character ( \ ) has a special purpose in JavaScript strings. Combined with the character that follows it, it represents a character that is not otherwise representable within the string. For example, \n is an escape sequence that represents a newline character.

```javascript
console.log('You can\'t do that!')
```
```bash
## You can't do that!
```

To determine the length of a string we can use the `.length` property of the string. 

```javascript
a_text = "This is a sentence."

console.log("Current sentence has " + a_text.length + " characters")
```
```bash
## Current sentence has 19 characters
```

In addition, the JavaScript provides a rich api for working with strings.

```javascript
console.log(a_text.substring(1,4)); // the 2nd, 3rd, and 4th characters
console.log(a_text.slice(1,4)); // idem, but different function
console.log(a_text.split(" ")); // split the string 
/* searching for a substring */
console.log(a_text.indexOf("This")); // position of first character of the substring
console.log(a_text.startsWith("This")); // => true: string starts with this substring
console.log(a_text.endsWith("sentence.")); // => true: string ends with this substring
console.log(a_text.includes("a")); // => true: string includes this substring
/* creating modified versions of a string */
console.log(a_text.replace("is ", "is not ")); // replace the first sub-string with the second
console.log(a_text.toLowerCase()); // to lower case
console.log(a_text.toUpperCase()); // to upper case
console.log("\u006E\u0303o".normalize()); // => ño: normalize to unicocde
/* String padding functions in ES2017 */
console.log("x".padStart(3)); // => " x": add
console.log("x".padEnd(3)); // => "x ": add
console.log("x".padStart(3, "*")); // => "**x": add
console.log("x".padEnd(3, "-")); // => "x--": add
/* white space trimming */ 
x = "        Hello world!            ";
console.log(x.trim());
console.log(x.trimStart());
console.log(x.trimEnd());
```
```bash
## his
## ño
##   x
## x  
## **x
## x--
## Hello world!
## Hello world!            
##         Hello world!
```

As discussed above, strings are nothing but arrays composed with 16-bit characters. Consequently, they may be index link arrays.

```javascript
a_text[0] + a_text[1] + a_text[2] + a_text[3];
```
```bash
## [32m'This'[39m
```

```javascript
// with a for loop
new_text = ""
max_char = 4
for (let i = 0; i <= max_char; i++) {
    new_text += a_text[i]
}
console.log(new_text)
```
```bash
## This 
```