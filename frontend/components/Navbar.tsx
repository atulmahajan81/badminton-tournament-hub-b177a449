import Link from 'next/link';

const Navbar = () => {
  return (
    <nav className="bg-white shadow-sm">
      <div className="container mx-auto p-4">
        <div className="flex justify-between">
          <div>
            <Link href="/">
              <a className="text-xl font-bold">Badminton Tournament Hub</a>
            </Link>
          </div>
          <div>
            <Link href="/auth/login">
              <a className="text-blue-500">Login</a>
            </Link>
          </div>
        </div>
      </div>
    </nav>
  );
};

export default Navbar;