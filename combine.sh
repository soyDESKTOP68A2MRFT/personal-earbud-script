#!/bin/sh

# Verificar que se haya pasado un argumento
if [ -z "$1" ]; then
  echo "Error: No se especificó una acción. Usa 'connect', 'sync', 'unsync' o 'disconnect'."
  exit 1
fi

# Función para sincronizar audífonos
sync_audifonos() {
  echo "Sincronizando los audífonos..."
  pactl load-module module-combine-sink slaves=bluez_sink.41_42_B0_38_00_23.a2dp_sink,bluez_sink.41_42_6C_C2_F6_4A.a2dp_sink
  if [ $? -eq 0 ]; then
    echo "Audífonos sincronizados con éxito."
  else
    echo "Error al sincronizar los audífonos."
    exit 1
  fi
}

# Función para conectar audífonos
connect_audifonos() {
  echo "Intentando conectar los audífonos..."
  bluetoothctl connect 41:42:B0:38:00:23
  bluetoothctl connect 41:42:6C:C2:F6:4A
  if [ $? -eq 0 ]; then
    echo "Audífonos conectados con éxito."
  else
    echo "Error al conectar los audífonos."
    exit 1
  fi
}

# Función para desconectar audífonos
disconnect_audifonos() {
  echo "Intentando desconectar los audífonos..."
  bluetoothctl disconnect 41:42:B0:38:00:23
  bluetoothctl disconnect 41:42:6C:C2:F6:4A
  if [ $? -eq 0 ]; then
    echo "Audífonos desconectados con éxito."
  else
    echo "Error al desconectar los audífonos."
    exit 1
  fi
}

# Función para desincronizar audífonos
unsync_audifonos() {
  echo "Desincronizando los audífonos..."
  pactl unload-module module-combine-sink
  if [ $? -eq 0 ]; then
    echo "Audífonos desincronizados con éxito."
  else
    echo "Error al desincronizar los audífonos."
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
  unsync)
    unsync_audifonos
    ;;
  *)
    echo "Error: Acción no reconocida. Usa 'sync', 'connect', 'unsync' o 'disconnect'."
    exit 1
    ;;
esac




