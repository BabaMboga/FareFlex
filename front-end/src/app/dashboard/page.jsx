import UserInfo from "@/components/UserInfo";
import React from 'react';
import Head from 'next/head';
import Image from 'next/image';
import UserInfo from '../components/UserInfo';
import TransactionHistory from '../components/TransactionHistory';
import styles from '../styles/Dashboard.module.css';

const Dashboard = () => {
  const user = {
    name: 'John Doe',
    balance: '10,000 KES',
    picture: '/profile.jpg', // Add a profile picture in the public folder
  };

  return (
    <div className={styles.container}>
      <Head>
        <title>Dashboard</title>
        <meta name="description" content="User Dashboard" />
        <link rel="icon" href="/favicon.ico" />
      </Head>
      <main className={styles.main}>
        <div className={styles.profile}>
          <Image src={user.picture} alt={user.name} width={100} height={100} className={styles.profileImage} />
          <h1>{user.name}</h1>
          <h2>Balance: {user.balance}</h2>
        </div>
        <TransactionHistory />
        <div className={styles.paymentInstructions}>
          <h3>Payment Instructions</h3>
          <div className={styles.paymentMethod}>
            <h4>M-Pesa</h4>
            <p>1. Go to the M-Pesa menu on your phone.</p>
            <p>2. Select Lipa na M-Pesa.</p>
            <p>3. Enter Paybill Number: 123456.</p>
            <p>4. Enter Account Number: your phone number.</p>
            <p>5. Enter Amount.</p>
            <p>6. Enter your M-Pesa PIN and send.</p>
          </div>
          <div className={styles.paymentMethod}>
            <h4>Bank Transfer</h4>
            <p>1. Log in to your online banking account.</p>
            <p>2. Select Transfer Funds.</p>
            <p>3. Enter Bank Name: ABC Bank.</p>
            <p>4. Enter Account Number: 9876543210.</p>
            <p>5. Enter Amount.</p>
            <p>6. Confirm the transfer details and submit.</p>
          </div>
        </div>
      </main>
    </div>
  );
};



export default function Dashboard() {
  return <UserInfo />;
}