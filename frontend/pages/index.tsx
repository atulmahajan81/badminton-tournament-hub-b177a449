import Head from 'next/head';
import { useQuery } from 'react-query';
import { fetchTournaments } from '@/lib/hooks/useTournaments';
import TournamentCard from '@/components/TournamentCard';
import LoadingSpinner from '@/components/LoadingSpinner';
import ErrorBoundary from '@/components/ErrorBoundary';

export default function Dashboard() {
  const { data, error, isLoading } = useQuery('tournaments', fetchTournaments);

  return (
    <div>
      <Head>
        <title>Dashboard - Badminton Tournament Hub</title>
      </Head>
      <ErrorBoundary>
        <div className="p-4">
          <h1 className="text-2xl font-bold mb-4">Tournaments</h1>
          {isLoading ? (
            <LoadingSpinner />
          ) : error ? (
            <div>Error loading tournaments</div>
          ) : (
            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
              {data.tournaments.map((tournament: any) => (
                <TournamentCard key={tournament.id} tournament={tournament} />
              ))}
            </div>
          )}
        </div>
      </ErrorBoundary>
    </div>
  );
}