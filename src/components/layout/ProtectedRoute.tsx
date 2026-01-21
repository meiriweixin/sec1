import { useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import { useStore } from '@/lib/store';

interface ProtectedRouteProps {
  children: React.ReactNode;
  adminOnly?: boolean;
}

export function ProtectedRoute({ children, adminOnly = false }: ProtectedRouteProps) {
  const { user, _hasHydrated } = useStore();
  const navigate = useNavigate();

  useEffect(() => {
    // Wait for store hydration before checking auth
    if (!_hasHydrated) {
      return;
    }

    // Check if user is logged in
    if (!user) {
      navigate('/login');
      return;
    }

    // Check if admin access is required
    if (adminOnly && !user.isAdmin) {
      navigate('/dashboard');
      return;
    }
  }, [user, _hasHydrated, adminOnly, navigate]);

  // Show nothing while hydrating or checking auth
  if (!_hasHydrated || !user) {
    return null;
  }

  // Show nothing if admin required but user is not admin
  if (adminOnly && !user.isAdmin) {
    return null;
  }

  return <>{children}</>;
}
