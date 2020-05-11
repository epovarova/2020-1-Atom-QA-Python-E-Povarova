#!/bin/bash
FILE=$1
if [ ! -f "$FILE" ]; then
  echo ERROR: $FILE does not exist 1>&2
  exit 1
fi
RESULT="sh_result.txt"


printf "%s %s\n\n" "total count is " "$(wc -l "$FILE" | cut -f1 -d' ')" > $RESULT

for method in $(awk '{print $6}' "$FILE" | sort | uniq)
do
  printf "%s %s\n\n" "count of ${method#*\"} is" "$(grep -c "${method#*\"}" "$FILE")" >> $RESULT
done

printf "%s\n%s\n\n" "top 10 largest queries: " "$(sort -rnk10 $FILE | awk -F' "|" | ' 'FNR < 11 {print $FILE0,$6,$7,$FILE,$4,$5}')" >> $RESULT

awk -F' "| ' '$9~/^4[0-9][0-9]$/ {print $7":"$9}' $FILE | awk '{A[$FILE]++}END{for(i in A)print i" is repeated "A[i]}' | sort -rnk4 | head -n 10 >> $RESULT

awk -F' "| ' '$9~/^3[0-9][0-9]$/ {print $7":"$9}' $FILE | awk '{A[$FILE]++}END{for(i in A)print i" is repeated "A[i]}' | sort -rnk4 | head -n 10 >> $RESULT
