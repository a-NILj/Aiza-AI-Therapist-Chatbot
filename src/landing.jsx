import LOGO from './assets/LOGO.png'
import Hero from './assets/Hero.png'
function LandingPage() {
  return (
    <div className="min-h-screen bg-blue-100 flex flex-col">
      {/* Header */}
      <header className="flex justify-between items-center p-6 bg-blue-100">
        <div className="text-2xl font-bold text-gray-700">
          {/* Logo Placeholder */}
          <span className="flex items-center space-x-2">
            <img src={LOGO} alt="Logo" className="h-8 w-8"/>
            <span>AIZA</span>
          </span>
        </div>
        <nav className="space-x-8 text-gray-700 hidden md:flex">
          <a href="#home" className="hover:text-blue-600">Home</a>
          <a href="#about" className="hover:text-blue-600">About Us</a>
          <a href="#testimonials" className="hover:text-blue-600">Testimonials</a>
          <a href="#contact" className="hover:text-blue-600">Contact Us</a>
        </nav>
        <button className="px-4 py-2 bg-white text-blue-600 rounded-full border border-blue-600 hover:bg-blue-50">
          SignIn/SignUp
        </button>
      </header>

      {/* Hero Section */}
      <main className="flex-grow flex flex-col items-center justify-center text-center px-6 md:px-0">
        <div className="relative w-full max-w-lg">
          {/* Illustration */}
          <img
            src={Hero} 
            alt="AI Wellness Assistant" 
            className="w-full"
          />
        </div>

        <h1 className="text-3xl md:text-4xl font-bold text-gray-800 mt-8">
          Your AI-Powered Path to Mental Wellness
        </h1>
        <p className="text-gray-600 mt-4 max-w-md">
          Accessible, private, and available anytime you need support.
        </p>
        <button className="mt-6 px-6 py-3 bg-red-600 text-white rounded-full hover:bg-red-700 transition duration-300">
          Start your Journey
        </button>
      </main>
    </div>
  );
}

export default LandingPage;
