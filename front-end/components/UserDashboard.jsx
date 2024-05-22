"use client";

import { signOut } from "next-auth/react";
import { useSession } from "next-auth/react";

import { useState } from 'react';

export default function UserDashboard() {
  const [isDark, setIsDark] = useState(false);
  const { data: session } = useSession();

  return (
    <div className={isDark ? 'dark' : ''}>
      <div className="min-h-screen flex flex-col antialiased bg-white dark:bg-gray-700 text-black dark:text-white">
        {/* Header */}
        <div className="fixed w-full flex items-center justify-between h-14 text-white z-10 bg-green-500 dark:bg-gray-800">
          <div className="flex items-center pl-3 w-14 md:w-64 h-14">
            <img className="w-7 h-7 md:w-10 md:h-10 mr-2 rounded-md" src="https://therminic2018.eu/wp-content/uploads/2018/07/dummy-avatar.jpg" alt="Avatar" />
            <div className="hidden md:block">{session?.user?.name}</div>
          </div>
          <div className="flex justify-between items-center h-14 header-right">
            <div className="bg-white rounded flex items-center w-full max-w-xl mr-4 p-2 shadow-sm border border-gray-200">
              <button className="outline-none focus:outline-none">
                <svg className="w-5 text-gray-600 h-5 cursor-pointer" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z" />
                </svg>
              </button>
              <input type="search" placeholder="Search" className="w-full pl-3 text-sm text-black outline-none bg-transparent" />
            </div>
            <ul className="flex items-center">
              <li>
                <button onClick={() => setIsDark(!isDark)} className="group p-2 transition-colors duration-200 rounded-full shadow-md bg-blue-200 dark:bg-gray-50 dark:text-gray-900">
                  {isDark ? (
                    <svg className="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path d="M11.049 2.927c.3-.921 1.603-.921 1.902 0l1.519 4.674a1 1 0 00.95.69h4.915c.969 0 1.371 1.24.588 1.81l-3.976 2.888a1 1 0 00-.363 1.118l1.518 4.674c.3.922-.755 1.688-1.538 1.118l-3.976-2.888a1 1 0 00-1.176 0l-3.976 2.888c-.783.57-1.838-.197-1.538-1.118l1.518-4.674a1 1 0 00-.363-1.118l-3.976-2.888c-.784-.57-.38-1.81.588-1.81h4.914a1 1 0 00.951-.69l1.519-4.674z" />
                    </svg>
                  ) : (
                    <svg className="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path d="M20.354 15.354A9 9 0 018.646 3.646 9.003 9.003 0 0012 21a9.003 9.003 0 008.354-5.646z" />
                    </svg>
                  )}
                </button>
              </li>
              <li><div className="block w-px h-6 mx-3 bg-gray-400 dark:bg-gray-700"></div></li>
              <button onClick={() => signOut()}>
                <a  href="#" className="flex items-center mr-4 hover:text-blue-100">
                  <span className="inline-flex mr-1">
                    <svg className="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path d="M17 16l4-4m0 0l-4-4m4 4H7m6 4v1a3 3 0 01-3 3H6a3 3 0 01-3-3V7a3 3 0 013-3h4a3 3 0 013 3v1" />
                    </svg>
                  </span>
                  Logout
                </a>
              </button>
            </ul>
          </div>
        </div>
        {/* Sidebar */}
        <div className="fixed flex flex-col top-14 left-0 w-14 hover:w-64 md:w-64 bg-green-600 dark:bg-gray-900 h-full text-white transition-all duration-300 border-none z-10">
          <div className="overflow-y-auto overflow-x-hidden flex flex-col justify-between flex-grow">
            <ul className="flex flex-col py-4 space-y-1">
              
              <li>
                <a href="#" className="relative flex flex-row items-center h-11 hover:bg-green-500 dark:hover:bg-gray-600 text-white-600 hover:text-white-800 border-l-4 border-transparent hover:border-green-100 dark:hover:border-gray-800 pr-6">
                  <span className="inline-flex justify-center items-center ml-4">
                    <svg className="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path d="M3 12l2-2m0 0l7-7 7 7M5 10v10a1 1 0 001 1h3m10-11l2 2m-2-2v10a1 1 0 01-1 1h-3m-6 0a1 1 0 001-1v-4a1 1 0 011-1h2a1 1 0 011 1v4a1 1 0 001 1m-6 0h6" />
                    </svg>
                  </span>
                  <span className="ml-2 text-xl tracking-wide truncate">Dashboard</span>
                </a>
              </li>
              <li>
                <a href="#" className="relative flex flex-row items-center h-11 hover:bg-green-500 dark:hover:bg-gray-600 text-white-600 hover:text-white-800 border-l-4 border-transparent hover:border-green-100 dark:hover:border-gray-800 pr-6">
                  <span className="inline-flex justify-center items-center ml-4">
                    <svg className="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path d="M20 13V6a2 2 0 00-2-2H6a2 2 0 00-2 2v7m16 0v5a2 2 0 01-2 2H6a2 2 0 01-2-2v-5m16 0H4" />
                    </svg>
                  </span>
                  <span className="ml-2 text-xl tracking-wide truncate">Board</span>
                  <span className="hidden md:block px-2 py-0.5 ml-auto text-xs font-medium tracking-wide text-red-500 bg-red-50 rounded-full">New</span>
                </a>
              </li>

              <li>
                <a href="#" className="relative flex flex-row items-center h-11 hover:bg-green-500 dark:hover:bg-gray-600 text-white-600 hover:text-white-800 border-l-4 border-transparent hover:border-green-100 dark:hover:border-gray-800 pr-6">
                  <span className="inline-flex justify-center items-center ml-4">
                    <svg className="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path d="M5 3v16a1 1 0 001 1h12a1 1 0 001-1V3m-1 10H6m4-5H6m4-5H6m6 10h2m-2-5h6m-6-5h6" />
                    </svg>
                  </span>
                  <span className="ml-2 text-xl tracking-wide truncate">Tasks</span>
                  <span className="hidden md:block px-2 py-0.5 ml-auto text-xs font-medium tracking-wide text-blue-500 bg-blue-50 rounded-full">76</span>
                </a>
              </li>
            
            <li>
              <a href="#" className="relative flex flex-row items-center h-11 hover:bg-green-500 dark:hover:bg-gray-600 text-white-600 hover:text-white-800 border-l-4 border-transparent hover:border-green-100 dark:hover:border-gray-800 pr-6">
                <span class="inline-flex justify-center items-center ml-4">
                  <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 17h5l-1.405-1.405A2.032 2.032 0 0118 14.158V11a6.002 6.002 0 00-4-5.659V5a2 2 0 10-4 0v.341C7.67 6.165 6 8.388 6 11v3.159c0 .538-.214 1.055-.595 1.436L4 17h5m6 0v1a3 3 0 11-6 0v-1m6 0H9"></path></svg>
                </span>
                <span class="ml-2 text-xl tracking-wide truncate">Notifications</span>
                <span class="hidden md:block px-2 py-0.5 ml-auto text-xs font-medium tracking-wide text-red-500 bg-red-50 rounded-full">1.2k</span>
              </a>
            </li>
            <li class="px-5 hidden md:block">
              <div class="flex flex-row items-center mt-5 h-8">
                <div class="text-xl font-light tracking-wide text-gray-400 uppercase">Settings</div>
              </div>
            </li>
            <li>
              <a href="#" class="relative flex flex-row items-center h-11 focus:outline-none hover:bg-green-500 dark:hover:bg-gray-600 text-white-600 hover:text-white-800 border-l-4 border-transparent hover:border-green-100 dark:hover:border-gray-800 pr-6">
                <span class="inline-flex justify-center items-center ml-4">
                  <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z"></path></svg>
                </span>
                <span class="ml-2 text-xl tracking-wide truncate">Profile</span>
              </a>
            </li>
           
            <li>
              <a href="#" class="relative flex flex-row items-center h-11 focus:outline-none hover:bg-green-500 dark:hover:bg-gray-600 text-white-600 hover:text-white-800 border-l-4 border-transparent hover:border-green-100 dark:hover:border-gray-800 pr-6">
                <span class="inline-flex justify-center items-center ml-4">
                  <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10.325 4.317c.426-1.756 2.924-1.756 3.35 0a1.724 1.724 0 002.573 1.066c1.543-.94 3.31.826 2.37 2.37a1.724 1.724 0 001.065 2.572c1.756.426 1.756 2.924 0 3.35a1.724 1.724 0 00-1.066 2.573c.94 1.543-.826 3.31-2.37 2.37a1.724 1.724 0 00-2.572 1.065c-.426 1.756-2.924 1.756-3.35 0a1.724 1.724 0 00-2.573-1.066c-1.543.94-3.31-.826-2.37-2.37a1.724 1.724 0 00-1.065-2.572c-1.756-.426-1.756-2.924 0-3.35a1.724 1.724 0 001.066-2.573c-.94-1.543.826-3.31 2.37-2.37.996.608 2.296.07 2.572-1.065z"></path>
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"></path>
                  </svg>
                </span>
                <span class="ml-2 text-xl tracking-wide truncate">Settings</span>
              </a>
            </li>
            </ul>
            <p className="mb-14 px-5 py-3 hidden md:block text-center text-xs">Copyright @2024</p>
          </div>
        </div>
        {/* Content */}
        <div className="flex-grow text-black dark:text-white p-6 md:ml-64 mt-14">
          <h1 className="text-4xl font-semibold mb-6">Lipa Fare</h1>
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
            {/* Example card */}
            <div className="bg-white dark:bg-gray-800 p-5 rounded-lg shadow">
              <h2 className="text-xl font-bold">Card Title</h2>
              <p className="mt-2">This is an example card content.</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

