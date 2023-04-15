import '@/styles/globals.css';
import { ThirdwebProvider } from '@thirdweb-dev/react';

export default function App({ Component, pageProps }) {
  return (
    <ThirdwebProvider
      infuraApiKey="https://polygon-mainnet.infura.io/v3/27411c613725409fa8aab00b844becdd"
      activeChain={137}
    >
      <Component {...pageProps} />
    </ThirdwebProvider>
  );
}
