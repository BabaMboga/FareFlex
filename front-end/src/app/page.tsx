import Image from 'next/image';
import Link from 'next/link';
import EmailSignIn from "@/components/AuthForms/EmailSignIn";

export default function Home() {
  return (
    <div className="flex min-h-screen">
      {/* Main container with a flex layout */}

      <main className="flex-1 p-8">
        {/* Main content area */}
        
        <div className="max-w-3xl mx-auto">
          {/* Centered container */}

          <EmailSignIn />
          
          <header className="text-center mb-12">
            {/* Header section */}
            <h1 className="text-4xl font-bold text-green-700 mb-4">
              Welcome to Our Business Page
            </h1>
            <p className="text-gray-600">
              We provide top-quality services to meet your needs.
            </p>
            <div className="mt-6">
              {/* Image section */}
              <Image src="ian-dooley-DJ7bWa-Gwks-unsplash.jpg" alt="Business Image" width={600} height={400} />
            </div>
          </header>
          
          <section className="bg-green-100 rounded-lg p-6 mb-12">
            {/* User info section */}
            <h2 className="text-2xl font-semibold text-green-700 mb-4">User Information</h2>
            <p className="text-gray-600">Name: John Doe</p>
            <p className="text-gray-600">Balance: $1,234.56</p>
          </section>
          
          <section className="grid grid-cols-1 md:grid-cols-2 gap-8 mb-12">
            {/* Services section */}
            <div className="bg-green-100 rounded-lg p-6">
              <h2 className="text-xl font-semibold text-green-700 mb-4">Service 1</h2>
              <p className="text-gray-600">
                Description of Service 1. Lorem ipsum dolor sit amet, consectetur adipiscing elit.
              </p>
            </div>
            <div className="bg-green-100 rounded-lg p-6">
              <h2 className="text-xl font-semibold text-green-700 mb-4">Service 2</h2>
              <p className="text-gray-600">
                Description of Service 2. Lorem ipsum dolor sit amet, consectetur adipiscing elit.
              </p>
            </div>
          </section>
          
          <section className="mb-12">
            {/* Payment instructions section */}
            <h2 className="text-2xl font-semibold text-green-700 mb-4">How to Pay</h2>
            <div className="bg-green-100 rounded-lg p-6 mb-6">
              <h3 className="text-xl font-semibold text-green-700 mb-4">Mpesa</h3>
              <p className="text-gray-600">Step 1: Go to the Mpesa menu.</p>
              <p className="text-gray-600">Step 2: Select Pay Bill.</p>
              <p className="text-gray-600">Step 3: Enter Business Number: 123456.</p>
              <p className="text-gray-600">Step 4: Enter Account Number: Your Account Number.</p>
              <p className="text-gray-600">Step 5: Enter Amount and confirm.</p>
            </div>
            <div className="bg-green-100 rounded-lg p-6">
              <h3 className="text-xl font-semibold text-green-700 mb-4">Bank Transfer</h3>
              <p className="text-gray-600">Step 1: Log in to your online banking.</p>
              <p className="text-gray-600">Step 2: Select Transfer Funds.</p>
              <p className="text-gray-600">Step 3: Enter our Bank Account Number: 987654321.</p>
              <p className="text-gray-600">Step 4: Enter the amount and confirm.</p>
            </div>
          </section>
          
          <section>
            {/* Contact section */}
            <h2 className="text-2xl font-semibold text-green-700 mb-4">Contact Us</h2>
            <p className="text-gray-600">For inquiries, please contact us at:</p>
            <p className="text-gray-600">Email: info@business.com</p>
            <p className="text-gray-600">Phone: 123-456-7890</p>
          </section>
          
        </div>
      </main>
    </div>
  );
}
