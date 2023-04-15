import { Container, Group } from '@mantine/core';

const cardData = [
  {
    id: 1,
    name: 'Card 1',
    address: '0x1234567890',
    status: 'Active',
  },
  {
    id: 2,
    name: 'Card 1',
    address: '0x1234567890',
    status: 'Active',
  },
  {
    id: 3,
    name: 'Card 1',
    address: '0x1234567890',
    status: 'Active',
  },
  {
    id: 4,
    name: 'Card 1',
    address: '0x1234567890',
    status: 'Active',
  },
];

const Hero = () => {
  return (
    <Container size="lg">
      <Group position="center" grow>
        {cardData.map((card) => (
          <div key={card.id} className="border border-gray-300 rounded-md p-4">
            <h1 className="text-xl font-semibold">{card.name}</h1>
            <p>{card.address}</p>
            <p>{card.status}</p>
          </div>
        ))}
      </Group>
    </Container>
  );
};

export default Hero;
