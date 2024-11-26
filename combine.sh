#!/bin/sh

# Verificar que se haya pasado un argumento
if [ -z "$1" ]; then
  echo "Error: No se especificó una acción. Usa 'connect' para conectar, 'sync' para sincronizar o 'disconnect' para desconectar."
  exit 1
fi

# Función para sincronizar audífonos
sync_audifonos() {
  echo "Sincronizando los audífonos..."
  # El comando pactl para sincronizar los dos audífonos
  pactl load-module module-combine-sink slaves=bluez_sink.<YOURMAC>.a2dp_sink,bluez_sink.<YOURMAC>.a2dp_sink
  if [ $? -eq 0 ]; then
    echo "Audífonos sincronizados con éxito."
  else
    echo "Error al sincronizar los audífonos."
    exit 1
  fi
}

# Función para conectar audífonos
connect_audifonos() {
  # Reemplaza con la lógica para sincronizar los audífonos
  echo "Intentando sincronizar los audífonos..."
  # Aquí agregas los comandos específicos de sincronización, por ejemplo:
  bluetoothctl connect 41:42:B0:38:00:23
  bluetoothctl connect 41:42:6C:C2:F6:4A

  # Verificar si la sincronización fue exitosa
  if [ $? -eq 0 ]; then
    echo "Audífonos sincronizados con éxito."
    exit 0
  else
    echo "Error al sincronizar los audífonos."
    exit 1
  fi
}

# Función para desconectar audífonos
disconnect_audifonos() {
  # Reemplaza con la lógica para desconectar los audífonos
  echo "Intentando desconectar los audífonos..."
  bluetoothctl disconnect 41:42:B0:38:00:23
  bluetoothctl disconnect 41:42:6C:C2:F6:4A

  # Verificar si la desconexión fue exitosa
  if [ $? -eq 0 ]; then
    echo "Audífonos desconectados con éxito."
    exit 0
  else
    echo "Error al desconectar los audífonos."
    exit 1
  fi
}

# Lógica para manejar las acciones según el argumento
case "$1" in
  sync)
    sync_audifonos
    ;;
  connect)
    connect_audifonos
    ;;
  disconnect)
    disconnect_audifonos
    ;;
  *)
    echo "Error: Acción no reconocida. Usa 'sync' para sincronizar o 'connect' para conectar, y 'disconnect' para desconectar."
    exit 1
    ;;
esac




