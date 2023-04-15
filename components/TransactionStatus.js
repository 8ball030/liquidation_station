import {
  Alert,
  Container,
  Modal,
  Popover,
  Progress,
  Table,
} from '@mantine/core';

const transactions = [
  {
    id: 1,
    title: 'Opening Position',
    data: [
      {
        id: 11,
        address: '0x12345678913434134',
        assets: 'ETH',
        hf: -1,
      },
      {
        id: 12,
        address: '0x12345678913434134',
        assets: 'ETH',
      },
      {
        id: 13,
        address: '0x12345678913434134',
      },
    ],
  },
  {
    id: 2,
    title: 'Pending',
    data: [
      {
        id: 11,
        address: '0x12345678913434134',
        assets: 'ETH',
        hf: 2,
      },
      {
        id: 12,
        address: '0x12345678913434134',
        assets: 'ETH',
      },
      {
        id: 13,
        address: '0x12345678913434134',
      },
    ],
  },
  {
    id: 3,
    title: 'Done',
    data: [
      {
        id: 11,
        assets: 'ETH',
        address: '0x12345678913434134',
        hf: 0,
      },
      {
        id: 12,
        address: '0x12345678913434134',
        assets: 'ETH',
      },
      {
        id: 13,
        address: '0x12345678913434134',
      },
    ],
  },
];

const TransactionStatus = () => {
  return (
    <Container size="lg" padding="md" className="mt-10">
      <Table
        withColumnBorders
        verticalSpacing="md"
        withBorder
        className="bg-neutral-100"
        //    highlightOnHover
      >
        <thead className="text-lg">
          <tr className="bg-neutral-300">
            {transactions.map((transaction) => (
              <th key={transaction.id} className="mr-2">
                {transaction.title}
              </th>
            ))}
          </tr>
        </thead>
        <tbody>
          {transactions.map((transaction) => (
            <tr className="cursor-pointer ">
              {transaction.data.map((data) => (
                <td key={transaction.id} className="hover:bg-neutral-200">
                  <div
                    key={data.id}
                    className="flex flex-col justify-between"
                    {...(data.id === 13 && {
                      onClick: () => alert(`Transaction Hash: ${data.address}`),
                    })}
                  >
                    <span>Transaction Hash: {data.address}</span>
                    {data.assets && <span>Assets: {data.assets}</span>}
                    {(data.hf >= -1 || data.hf <= 3) && (
                      <span className="flex flex-col space-y-2">
                        <span>Health Factor : {data.hf}</span>
                        <Progress
                          value={(data.hf + 1) * 20}
                          label={data.hf}
                          size="xl"
                          radius="sm"
                          color="violet"
                          animate
                        />
                      </span>
                    )}
                  </div>
                </td>
              ))}
            </tr>
          ))}
        </tbody>
      </Table>
    </Container>
  );
};

export default TransactionStatus;
