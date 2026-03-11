import { useRouter } from 'next/router';
import { useQuery } from 'react-query';
import { fetchTournamentById } from '@/lib/hooks/useTournaments';
import LoadingSpinner from '@/components/LoadingSpinner';
import ErrorBoundary from '@/components/ErrorBoundary';

const TournamentDetail = () => {
  const router = useRouter();
  const { id } = router.query;
  const { data, error, isLoading } = useQuery(['tournament', id], () => fetchTournamentById(id as string), { enabled: !!id });

  return (
    <div>
      <ErrorBoundary>
        {isLoading ? (
          <LoadingSpinner />
        ) : error ? (
          <div>Error loading tournament details</div>
        ) : (
          <div className="p-4">
            <h1 className="text-2xl font-bold mb-4">{data.name}</h1>
            <p>Location: {data.location}</p>
            <p>Date: {new Date(data.date).toLocaleDateString()}</p>
            <p>Rules: {data.rules}</p>
          </div>
        )}
      </ErrorBoundary>
    </div>
  );
};

export default TournamentDetail;