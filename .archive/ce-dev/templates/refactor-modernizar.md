---
description: "Refactoriza y moderniza codebase legacy aplicando mejores prácticas actuales"
allowedTools: ["Read", "Write", "Edit", "MultiEdit", "Grep", "Bash"]
extendedThinking: true
---

# Refactoring y Modernización de Código

Moderniza el codebase aplicando las mejores prácticas actuales, patrones modernos y optimizaciones de rendimiento.

**Alcance del refactoring**: $ARGUMENTS (component|module|full)

## Fase 1: Análisis del Estado Actual

### Auditoría del Código Legacy
Identificar áreas que necesitan modernización:

!find . -name "*.js" -o -name "*.jsx" | head -20 | while read file; do
  echo "=== Analizando $file ==="
  # Buscar patrones legacy
  grep -n "var " "$file" || echo "✅ No hay declaraciones var"
  grep -n "function(" "$file" | head -3 || echo "✅ No hay function declarations legacy"
  grep -n "componentDidMount\|componentWillMount" "$file" || echo "✅ No hay lifecycle methods legacy"
  echo ""
done

### Dependencias Obsoletas
!if [ -f "package.json" ]; then
  echo "=== Análisis de dependencias ==="
  npx npm-check-updates --format group
fi

### Patrones Anti-pattern
Buscar anti-patterns comunes:
- Componentes de clase sin estado
- Inline styles en lugar de CSS modules/styled-components
- Props drilling excesivo
- Mutación directa de estado
- Uso de índices como keys en listas

## Fase 2: Plan de Modernización

### Prioridades de Refactoring

#### 1. Crítico (Impacto Alto, Esfuerzo Bajo)
- Migrar de `var` a `const`/`let`
- Reemplazar function declarations con arrow functions
- Actualizar imports/exports a ES6+
- Eliminar código muerto

#### 2. Alto (Impacto Alto, Esfuerzo Medio)
- Migrar componentes de clase a funcionales con hooks
- Implementar TypeScript si no está presente
- Modernizar state management
- Optimizar bundle size

#### 3. Medio (Mejoras graduales)
- Mejorar patrones de rendering
- Implementar code splitting
- Agregar tests unitarios
- Optimizar performance

### Roadmap de Modernización
```markdown
## Semana 1-2: Fundamentos
- [ ] Migrar a ES6+ syntax
- [ ] Configurar ESLint/Prettier moderno
- [ ] Actualizar tooling de build

## Semana 3-4: Componentes
- [ ] Migrar componentes de clase a funcionales
- [ ] Implementar custom hooks
- [ ] Optimizar re-renders

## Semana 5-6: Arquitectura
- [ ] Mejorar state management
- [ ] Implementar code splitting
- [ ] Optimizar bundle

## Semana 7-8: Testing y Deploy
- [ ] Agregar tests comprehensivos
- [ ] Setup CI/CD moderno
- [ ] Performance monitoring
```

## Fase 3: Modernización de Sintaxis

### ES6+ Migrations

#### Variables y Scope
```javascript
// ❌ Legacy
var name = 'John';
var config = {
  api: 'https://api.example.com'
};

// ✅ Moderno
const name = 'John';
const config = {
  api: 'https://api.example.com'
};
```

#### Arrow Functions y Destructuring
```javascript
// ❌ Legacy
function processUser(user) {
  return {
    id: user.id,
    name: user.name,
    email: user.email
  };
}

// ✅ Moderno
const processUser = ({ id, name, email }) => ({ id, name, email });
```

#### Async/Await
```javascript
// ❌ Legacy con Promises
function fetchUserData(id) {
  return fetch(`/api/users/${id}`)
    .then(response => response.json())
    .then(data => data)
    .catch(error => console.error(error));
}

// ✅ Moderno con async/await
const fetchUserData = async (id) => {
  try {
    const response = await fetch(`/api/users/${id}`);
    return await response.json();
  } catch (error) {
    console.error('Error fetching user:', error);
    throw error;
  }
};
```

### Template Literals y String Methods
```javascript
// ❌ Legacy
var message = 'Hello ' + user.name + ', welcome to ' + app.name;

// ✅ Moderno
const message = `Hello ${user.name}, welcome to ${app.name}`;
```

## Fase 4: Modernización de React

### Componentes de Clase a Funcionales

#### Migration Pattern
```jsx
// ❌ Legacy Class Component
class UserProfile extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      user: null,
      loading: true,
      error: null
    };
  }

  async componentDidMount() {
    try {
      const user = await fetchUser(this.props.userId);
      this.setState({ user, loading: false });
    } catch (error) {
      this.setState({ error, loading: false });
    }
  }

  render() {
    const { user, loading, error } = this.state;
    
    if (loading) return <div>Loading...</div>;
    if (error) return <div>Error: {error.message}</div>;
    
    return <div>{user.name}</div>;
  }
}

// ✅ Modern Functional Component
const UserProfile = ({ userId }) => {
  const [user, setUser] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const loadUser = async () => {
      try {
        setLoading(true);
        const userData = await fetchUser(userId);
        setUser(userData);
      } catch (err) {
        setError(err);
      } finally {
        setLoading(false);
      }
    };

    loadUser();
  }, [userId]);

  if (loading) return <div>Loading...</div>;
  if (error) return <div>Error: {error.message}</div>;
  
  return <div>{user?.name}</div>;
};
```

### Custom Hooks para Lógica Reutilizable

#### useApi Hook
```javascript
// Custom hook para API calls
const useApi = (url, dependencies = []) => {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchData = async () => {
      try {
        setLoading(true);
        setError(null);
        const response = await fetch(url);
        const result = await response.json();
        setData(result);
      } catch (err) {
        setError(err);
      } finally {
        setLoading(false);
      }
    };

    fetchData();
  }, dependencies);

  return { data, loading, error };
};

// Uso del hook
const UserList = () => {
  const { data: users, loading, error } = useApi('/api/users');
  
  if (loading) return <Loading />;
  if (error) return <Error message={error.message} />;
  
  return (
    <ul>
      {users.map(user => (
        <li key={user.id}>{user.name}</li>
      ))}
    </ul>
  );
};
```

### Performance Optimizations

#### React.memo y useMemo
```jsx
// Memoización de componentes
const UserCard = React.memo(({ user, onEdit }) => {
  const displayName = useMemo(() => 
    `${user.firstName} ${user.lastName}`.trim(),
    [user.firstName, user.lastName]
  );

  return (
    <div className="user-card">
      <h3>{displayName}</h3>
      <button onClick={() => onEdit(user.id)}>Edit</button>
    </div>
  );
});

// useCallback para funciones estables
const UsersList = ({ users }) => {
  const handleEdit = useCallback((userId) => {
    // Logic for editing user
    console.log('Editing user:', userId);
  }, []);

  return (
    <div>
      {users.map(user => (
        <UserCard 
          key={user.id} 
          user={user} 
          onEdit={handleEdit}
        />
      ))}
    </div>
  );
};
```

## Fase 5: Modernización de Estado

### Context API vs Redux

#### React Context para Estado Simple
```jsx
// Context para tema
const ThemeContext = createContext();

export const ThemeProvider = ({ children }) => {
  const [theme, setTheme] = useState('light');
  
  const toggleTheme = useCallback(() => {
    setTheme(prev => prev === 'light' ? 'dark' : 'light');
  }, []);

  const value = useMemo(() => ({
    theme,
    toggleTheme
  }), [theme, toggleTheme]);

  return (
    <ThemeContext.Provider value={value}>
      {children}
    </ThemeContext.Provider>
  );
};

export const useTheme = () => {
  const context = useContext(ThemeContext);
  if (!context) {
    throw new Error('useTheme must be used within ThemeProvider');
  }
  return context;
};
```

#### Redux Toolkit para Estado Complejo
```javascript
// store/userSlice.js
import { createSlice, createAsyncThunk } from '@reduxjs/toolkit';

export const fetchUsers = createAsyncThunk(
  'users/fetchUsers',
  async (_, { rejectWithValue }) => {
    try {
      const response = await fetch('/api/users');
      return await response.json();
    } catch (error) {
      return rejectWithValue(error.message);
    }
  }
);

const userSlice = createSlice({
  name: 'users',
  initialState: {
    items: [],
    loading: false,
    error: null
  },
  reducers: {
    clearError: (state) => {
      state.error = null;
    }
  },
  extraReducers: (builder) => {
    builder
      .addCase(fetchUsers.pending, (state) => {
        state.loading = true;
        state.error = null;
      })
      .addCase(fetchUsers.fulfilled, (state, action) => {
        state.loading = false;
        state.items = action.payload;
      })
      .addCase(fetchUsers.rejected, (state, action) => {
        state.loading = false;
        state.error = action.payload;
      });
  }
});

export const { clearError } = userSlice.actions;
export default userSlice.reducer;
```

## Fase 6: TypeScript Migration

### Gradual TypeScript Adoption

#### tsconfig.json Setup
```json
{
  "compilerOptions": {
    "target": "ES2020",
    "module": "esnext",
    "lib": ["dom", "dom.iterable", "es6"],
    "allowJs": true,
    "skipLibCheck": true,
    "esModuleInterop": true,
    "allowSyntheticDefaultImports": true,
    "strict": true,
    "forceConsistentCasingInFileNames": true,
    "noFallthroughCasesInSwitch": true,
    "moduleResolution": "node",
    "resolveJsonModule": true,
    "isolatedModules": true,
    "noEmit": true,
    "jsx": "react-jsx",
    "incremental": true,
    "baseUrl": "src",
    "paths": {
      "@/*": ["./*"],
      "@/components/*": ["components/*"],
      "@/utils/*": ["utils/*"]
    }
  },
  "include": [
    "src"
  ]
}
```

#### Type Definitions
```typescript
// types/index.ts
export interface User {
  id: string;
  name: string;
  email: string;
  role: 'admin' | 'user' | 'moderator';
  createdAt: Date;
  updatedAt: Date;
}

export interface ApiResponse<T> {
  data: T;
  message?: string;
  error?: string;
}

export type UserCreateInput = Omit<User, 'id' | 'createdAt' | 'updatedAt'>;
export type UserUpdateInput = Partial<UserCreateInput>;

// Component Props Types
export interface UserCardProps {
  user: User;
  onEdit?: (userId: string) => void;
  onDelete?: (userId: string) => void;
  className?: string;
}
```

## Fase 7: Testing Modernization

### Modern Testing Setup

#### Jest Configuration
```javascript
// jest.config.js
module.exports = {
  testEnvironment: 'jsdom',
  setupFilesAfterEnv: ['<rootDir>/src/setupTests.ts'],
  moduleNameMapping: {
    '^@/(.*)$': '<rootDir>/src/$1',
    '\\.(css|less|scss|sass)$': 'identity-obj-proxy'
  },
  transform: {
    '^.+\\.(ts|tsx)$': 'ts-jest',
    '^.+\\.(js|jsx)$': 'babel-jest'
  },
  collectCoverageFrom: [
    'src/**/*.{ts,tsx}',
    '!src/**/*.d.ts',
    '!src/index.tsx'
  ],
  coverageThreshold: {
    global: {
      branches: 80,
      functions: 80,
      lines: 80,
      statements: 80
    }
  }
};
```

#### Modern Testing Patterns
```typescript
// UserCard.test.tsx
import { render, screen, fireEvent } from '@testing-library/react';
import userEvent from '@testing-library/user-event';
import { UserCard } from './UserCard';

const mockUser = {
  id: '1',
  name: 'John Doe',
  email: 'john@example.com',
  role: 'user' as const,
  createdAt: new Date(),
  updatedAt: new Date()
};

describe('UserCard', () => {
  it('displays user information correctly', () => {
    render(<UserCard user={mockUser} />);
    
    expect(screen.getByText('John Doe')).toBeInTheDocument();
    expect(screen.getByText('john@example.com')).toBeInTheDocument();
  });

  it('calls onEdit when edit button is clicked', async () => {
    const handleEdit = jest.fn();
    const user = userEvent.setup();
    
    render(<UserCard user={mockUser} onEdit={handleEdit} />);
    
    await user.click(screen.getByRole('button', { name: /edit/i }));
    
    expect(handleEdit).toHaveBeenCalledWith('1');
  });
});
```

## Fase 8: Build Tools Modernization

### Vite Migration from Create React App

#### vite.config.ts
```typescript
import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';
import { resolve } from 'path';

export default defineConfig({
  plugins: [react()],
  resolve: {
    alias: {
      '@': resolve(__dirname, 'src'),
    },
  },
  build: {
    sourcemap: true,
    rollupOptions: {
      output: {
        manualChunks: {
          vendor: ['react', 'react-dom'],
          router: ['react-router-dom'],
          ui: ['@mui/material', '@emotion/react']
        }
      }
    }
  },
  server: {
    port: 3000,
    proxy: {
      '/api': {
        target: 'http://localhost:8000',
        changeOrigin: true
      }
    }
  }
});
```

### ESLint y Prettier Modernos

#### .eslintrc.js
```javascript
module.exports = {
  extends: [
    'eslint:recommended',
    '@typescript-eslint/recommended',
    'react-hooks/recommended',
    'prettier'
  ],
  parser: '@typescript-eslint/parser',
  plugins: ['@typescript-eslint', 'react-hooks'],
  rules: {
    'react-hooks/rules-of-hooks': 'error',
    'react-hooks/exhaustive-deps': 'warn',
    '@typescript-eslint/no-unused-vars': 'error',
    '@typescript-eslint/explicit-function-return-type': 'off',
    'prefer-const': 'error',
    'no-var': 'error'
  },
  settings: {
    react: {
      version: 'detect'
    }
  }
};
```

## Implementación

### Checklist de Modernización
- [ ] Migrar sintaxis a ES6+
- [ ] Convertir componentes clase a funcionales
- [ ] Implementar custom hooks
- [ ] Agregar TypeScript gradualmente
- [ ] Modernizar testing setup
- [ ] Actualizar build tools
- [ ] Optimizar performance
- [ ] Configurar linting moderno
- [ ] Actualizar documentación
- [ ] Training del equipo

### Métricas de Éxito
- **Bundle Size**: Reducción del 20-30%
- **Performance**: Mejora en Core Web Vitals
- **Developer Experience**: Tiempo de build reducido
- **Code Quality**: Mayor cobertura de tests
- **Maintainability**: Menos bugs reportados

### Rollback Plan
- Mantener branches de backup
- Deploy gradual por módulos
- Monitoring de errores en producción
- Plan de reversión rápida si es necesario