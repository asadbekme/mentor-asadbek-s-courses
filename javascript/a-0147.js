// * Matndagi "A" va "Y" harflarining sonini aniqlang.

const countLetters = (str) => {
  let count1 = 0,
    count2 = 0;

  for (let i = 0; i < str.length; i++) {
    if (str[i] === "A") {
      count1 += 1;
    }
    if (str[i] === "Y") {
      count2 += 1;
    }
  }
  return [count1, count2];
};

console.log(countLetters("HAaYY gays")); // [1, 2]
console.log(countLetters("ALGORITMTUITUZ")); // [1, 0]
console.log(countLetters("YAKUNIYNAZORATISHI")); // [3, 2]
