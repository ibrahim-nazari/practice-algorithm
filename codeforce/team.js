function numDecodings(s) {
  const n = s.length;
  if (n === 0) return 0;

  const dp = new Array(n + 1).fill(0);
  dp[0] = 1;
  dp[1] = s[0] !== "0" ? 1 : 0;

  for (let i = 2; i <= n; i++) {
    // Check single digit decode possibility
    if (s[i - 1] !== "0") {
      dp[i] += dp[i - 1];
    }
    // Check two digit decode possibility
    const twoDigit = parseInt(s.substring(i - 2, i));
    if (twoDigit >= 10 && twoDigit <= 26) {
      dp[i] += dp[i - 2];
    }
  }

  return dp[n];
}

console.log(numDecodings("12")); // Output: 2
console.log(numDecodings("226")); // Output: 3
console.log(numDecodings("06")); // Output: 0
