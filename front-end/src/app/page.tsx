export default function Home() {
  return (
    <main className="flex min-h-screen flex-col items-center justify-between p-24">
      {/* Main container with flex layout, minimum height of the screen, centered items, and padding */}
      
      <div className="max-w-3xl w-full">
        {/* Container with a maximum width and full width on smaller screens */}
        
        <header className="text-center mb-12">
          {/* Header section */}
          <h1 className="text-4xl font-bold text-green-700 mb-4">
            Welcome to Our Business Page
          </h1>
          <p className="text-gray-600">
            We provide top-quality services to meet your needs.
          </p>
        </header>
        
        <section className="grid grid-cols-1 md:grid-cols-2 gap-8">
          {/* Services section - grid layout with 1 column on small screens and 2 columns on medium screens */}
          
          <div className="bg-green-100 rounded-lg p-6">
            {/* Service 1 */}
            <h2 className="text-xl font-semibold text-green-700 mb-4">Service 1</h2>
            <p className="text-gray-600">
              Description of Service 1 Lorem ipsum dolor sit amet, consectetur adipiscing elit.
            </p>
          </div>
          
          <div className="bg-green-100 rounded-lg p-6">
            {/* Service 2 */}
            <h2 className="text-xl font-semibold text-green-700 mb-4">Service 2</h2>
            <p className="text-gray-600">
              Description of Service 2 Lorem ipsum dolor sit amet, consectetur adipiscing elit.
            </p>
          </div>
        </section>
        
        <section className="mt-12">
          {/* Contact section */}
          <h2 className="text-2xl font-semibold text-green-700 mb-4">Contact Us</h2>
          <p className="text-gray-600">
            For inquiries, please contact us at:
          </p>
          <p className="text-gray-600">
            Email: info@business.com
          </p>
          <p className="text-gray-600">
            Phone: 123-456-7890
          </p>
        </section>
        
      </div>
    </main>
  );
}
