import React from 'react';
import styles from '../styles/TransactionHistory.module.css';

const TransactionHistory = () => {
  const transactions = [
    { id: 1, date: '2024-05-18', description: 'Grocery Shopping', amount: '-2,500 KES' },
    { id: 2, date: '2024-05-16', description: 'Salary', amount: '+15,000 KES' },
    { id: 3, date: '2024-05-10', description: 'Electricity Bill', amount: '-1,200 KES' },
  ];

  return (
    <div className={styles.transactionHistory}>
      <h3>Recent Transactions</h3>
      <ul>
        {transactions.map(transaction => (
          <li key={transaction.id} className={transaction.amount.startsWith('+') ? styles.credit : styles.debit}>
            <span>{transaction.date}</span>
            <span>{transaction.description}</span>
            <span>{transaction.amount}</span>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default TransactionHistory;
