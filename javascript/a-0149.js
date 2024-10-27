// * Matndagi 'NA' simvollari bilan tugaydigan so'zlar soni aniqlansin va bosib chiqarish dasturi tuzilsin.

const countAndPrintNA = (str) => {
  const words = str.split(" ");
  const NAWords = [];

  for (let i = 0; i < words.length; i++) {
    let word = words[i];
    if (word[word.length - 2] === "N" && word[word.length - 1] === "A") {
      NAWords.push(word);
    }
  }
  return [NAWords.length, NAWords];
};

console.log(countAndPrintNA("YaNA bahor keldi"));
console.log(countAndPrintNA("ANA MANA YANA asd HDFNAS"));
