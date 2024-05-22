"use client";

import Link from "next/link";
import { useState } from "react";
import { useRouter } from "next/navigation";

export default function RegisterForm() {
  const [first_name, setFirstName] = useState("");
  const [last_name, setLastName] = useState("");
  const [email, setEmail] = useState("");
  const [reference, setReference] = useState("");
  const [address, setAddress] = useState("");
  const [city, setCity] = useState("");
  const [state, setState] = useState("");
  const [zipcode, setZipcode] = useState("");
  const [country, setCountry] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");

  const router = useRouter();

  const handleSubmit = async (e) => {
    e.preventDefault();

    console.log("handleSubmit called");

    //try {
      //console.log("Fetching userExists...");
      //const resUserExists = await fetch("api/userExists", {
       // method: "POST",
        //headers: {
        //  "Content-Type": "application/json",
       // },
       // body: JSON.stringify({ email }),
     // });

      //console.log("Fetched userExists:", resUserExists);

      //const { user } = await resUserExists.json();

      

      console.log("Fetching register...");
      const res = await fetch("http://127.0.0.1:8000/register/", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          first_name,
          last_name,
          email,
          reference,
          address,
          city,
          state,
          zipcode,
          country,
          password,
        }),
      });

      console.log("Fetched register:", res);

      if (res.ok) {
        const form = e.target;
        const data = await res.json()
        console.log("Registration data:", data);
        form.reset();
        router.push("/");
      } else {
        console.log("Error during registration.");
      }
    } //catch (error) {
     // console.log("Error during registration: ", error);
    //}
 // };

 // Add closing parenthesis here

  return (
    <div className="grid place-items-center h-screen">
      <div className="shadow-lg p-5 rounded-lg border-t-4 border-green-400">
        <h1 className="text-xl font-bold my-4">Register</h1>

        <form onSubmit={handleSubmit} className="flex flex-col gap-3">
          <input
            onChange={(e) => setFirstName(e.target.value)}
            type="text"
            placeholder="First Name"
          />
            <input
            onChange={(e) => setLastName(e.target.value)}
            type="text"
            placeholder="Last Name"
          />
          <input
            onChange={(e) => setAddress(e.target.value)}
            type="text"
            placeholder="Address"
          />
                    <input
            onChange={(e) => setCity(e.target.value)}
            type="text"
            placeholder="City"
          />
                    <input
            onChange={(e) => setState(e.target.value)}
            type="text"
            placeholder="State"
          />
                    <input
            onChange={(e) => setZipcode(e.target.value)}
            type="text"
            placeholder="Zipcode"
          />
                    <input
            onChange={(e) => setCountry(e.target.value)}
            type="text"
            placeholder="Country"
          />
          <input
            onChange={(e) => setEmail(e.target.value)}
            type="text"
            placeholder="Email"
          />
          <input
            onChange={(e) => setPassword(e.target.value)}
            type="password"
            placeholder="Password"
          />
          <button className="bg-green-600 text-white font-bold cursor-pointer px-6 py-2">
            Register
          </button>

          {error && (
            <div className="bg-red-500 text-white w-fit text-sm py-1 px-3 rounded-md mt-2">
              {error}
            </div>
          )}

          <Link className="text-sm mt-3 text-right" href={"/"}>
            Already have an account? <span className="underline">Login</span>
          </Link>
        </form>
      </div>
    </div>
  );
}
