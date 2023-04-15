import Hero from '@/components/Hero';
import { Navbar } from '@/components/Navbar';
import TransactionStatus from '@/components/TransactionStatus';

const Home = () => {
  return (
    <main className="bg-neutral-900 min-h-screen">
      <Navbar links={[{ label: 'Home', link: '/' }]} />
      <Hero />
      <TransactionStatus />
    </main>
  );
};

export default Home;
