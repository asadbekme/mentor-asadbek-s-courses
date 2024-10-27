// * Matndagi 'A' dan boshlangan so'zlarni chop etuvchi dastur tuzilsin.
// Kiruvchi ma'lumotlar: Birinchi satrda s matn berilgan. Matn uzunligi 500 dan oshmaydi. Matnda katta va kichik lotin harflari va probel qatnashadi. Matndagi so'zlar probel bilan ajratilgan.

const logLetterABeginWords = (s) => {
  const words = s.split(" ");

  for (let i = 0; i < words.length; i++) {
    if (words[i][0] === "A") {
      console.log(words[i]);
    }
  }
};

logLetterABeginWords("I Am Asadbek");
logLetterABeginWords("Algoritm tuit uz");
logLetterABeginWords("ARTDJ Algoritm tuit uz dizayneri");
