// * 1. Sonning raqamlar yig'indisini hisoblovchi algoritm
const summa = (N) => {
  const numbersList = String(N).split(""); // Har bir raqamni ajratib, array qilish
  let totalSum = 0; // Yig'indini boshlang'ich 0 qilib belgilash

  // Har bir raqamni tekshirib, faqat raqamlarni yig'indiga qo'shish
  for (let number of numbersList) {
    if (!isNaN(number) && number !== " ") {
      // Agar raqam bo'lsa va probel bo'lmasa
      totalSum += parseInt(number);
    }
  }

  return totalSum;
};

// console.log(summa(1234567));
// console.log(summa(20013));

// * 2. String'dagi unli harflar(vowels) sonini hisoblovchi algoritm
const totalWovels = (s) => {
  const wovels = "AaOoIiUuEe";
  let count = 0;
  for (let i = 0; i < s.length; i++) {
    if (wovels.includes(s[i])) {
      count++;
    }
  }

  return count;
};

// console.log(totalWovels("Hello")); // 2
// console.log(totalWovels("I love JavaScript")); // 6
// console.log(totalWovels("Programming my LIFE")); // 5

// * 3. Ikkita string'dagi belgilarni ketma-ket birlashtiruvchi algoritm
const joinStrings = (s1, s2) => {
  let result = "";
  const maxLength = Math.max(s1.length, s2.length);

  for (let i = 0; i < maxLength; i++) {
    if (i < s1.length) {
      result += s1[i];
    }
    if (i < s2.length) {
      result += s2[i];
    }
  }

  return result;
};

console.log(joinStrings("abc", "xyz")); // axbycz
console.log(joinStrings("Hello!", "guy")); // Hgeulylo!
