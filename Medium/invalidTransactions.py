# https://leetcode.com/problems/invalid-transactions/

class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        invalid_transactions = []
        invalidSet = set()
        transaction_dict = {}
        count = 0
        for transaction in transactions:
            val = transaction.split(",")
            dict = {}
            dict['name'] = val[0]
            dict['time'] = val[1]
            dict['amt'] = val[2]
            dict['city'] = val[3]
            transaction_dict[count] = dict
            count += 1
        
        for i in range(0,len(transaction_dict)):
            valid = 1
            for j in range(i):
                time_diff = abs(int(transaction_dict[j]['time']) - int(transaction_dict[i]['time']))
                if transaction_dict[i]['name'] == transaction_dict[j]['name'] and time_diff <= 60 and transaction_dict[i]['city'] != transaction_dict[j]['city']:
                    if j not in invalidSet:
                        invalidSet.add(j)
                        invalid_transactions.append(transactions[j])
                    if i not in invalidSet:
                        invalidSet.add(i)
                        invalid_transactions.append(transactions[i])
                    valid = 0
            if valid == 1:
                if int(transaction_dict[i]['amt']) > 1000:
                    if i not in invalidSet:
                        invalidSet.add(i)
                        invalid_transactions.append(transactions[i])
                
        return invalid_transactions