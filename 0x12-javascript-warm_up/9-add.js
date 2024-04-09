function add (a, b) {
  const k = a + b;
  console.log(k);
}

add(Number(process.argv[2]), Number(process.argv[3]));
