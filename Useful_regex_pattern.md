## Useful regex patterns to remove from files:

1. To remove numbers:
    `\b[0-9][0-9][0-9]. `

2. To remove strs within square brackets
    `\[[^\]]*\] `

3. To remove play .. min 
    `\b\*min\b|\bPlay\b|\b[0-9]\s?min\b`

4. To remove ...min
    `\b[0-9][0-9]\s?min`